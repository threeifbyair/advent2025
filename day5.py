#!/usr/bin/env python3

import re
import sys, os

import adventday

class RangeLeaf:
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __str__(self):
        return f'[{self.low}-{self.high}]'

class RangeList:
    def __init__(self, low, high):
        self.root = [RangeLeaf(low, high)]

    def find_value(self, value):
        leaflen = len(self.root)
        leafpos = leaflen // 2
        leaf = self.root[leafpos]
        moveby = max(1, leaflen // 4)
        leaves_seen = set()
        while leaf is not None and (leaf.low > value or leaf.high < value):
            if leafpos in leaves_seen:
                leaf = None
                break
            leaves_seen.add(leafpos)
            if leaf.low > value:
                leafpos -= moveby
            elif leaf.high < value:
                leafpos += moveby
            else:
                break
            moveby = max(1, moveby // 2)
            if leafpos < 0 or leafpos >= len(self.root):
                break
            leaf = self.root[leafpos]
        if leafpos < 0:
            leafpos = 0
        elif leafpos >= len(self.root):
            leafpos = len(self.root) - 1
        if leaf is not None and (leaf.low > value or leaf.high < value):
            leaf = None
        return leaf, leafpos

    def add_range(self, low, high):
        self.lint()
        # First find where low is located.
        lowleaf, lowpos = self.find_value(low)

        if self.root[lowpos].low > high:
            # Insert before
            newleaf = RangeLeaf(low, high)
            self.root.insert(lowpos, newleaf)
        elif self.root[lowpos].high < low:
            # Insert after.
            newleaf = RangeLeaf(low, high)
            while lowpos < len(self.root) and self.root[lowpos].high < low:
                lowpos += 1
            self.root.insert(lowpos, newleaf)
        else:
            # Merge with this leaf.
            newleaf = self.root[lowpos]
            newleaf.low = min(newleaf.low, low)
            newleaf.high = max(newleaf.high, high)

        # OK, now let's merge with our neighbors.
        while lowpos > 0 and self.root[lowpos - 1].high + 1 >= newleaf.low:
            # Merge left.
            leftleaf = self.root[lowpos - 1]
            leftleaf.high = max(leftleaf.high, newleaf.high)
            self.root.pop(lowpos)
            lowpos -= 1
            newleaf = leftleaf
        while lowpos < len(self.root) - 1 and self.root[lowpos + 1].low - 1 <= newleaf.high:
            # Merge right.
            rightleaf = self.root[lowpos + 1]
            newleaf.high = max(newleaf.high, rightleaf.high)
            self.root.pop(lowpos + 1)
            lowpos += 1
            newleaf = rightleaf

        self.lint()

    def lint(self):
        for i in range(0, len(self.root)):
            if self.root[i].low > self.root[i].high:
                raise Exception(f'Lint error in range {i}: low > high')
            if i == 0:
                continue
            if self.root[i-1].high + 1 >= self.root[i].low:
                raise Exception(f'Lint error between {i-1} and {i}')

    def __str__(self):
        s = ''
        for leaf in self.root:
            s += f'[{leaf.low}-{leaf.high}] '
        return s.strip()

class Day5(adventday.AdventDay):
    def analyze_lines(self):
        self.ranges = []
        self.ingredients = []
        seen_blank = False
        for line in self.lines:
            if line.strip() == '':
                seen_blank = True
                continue
            if not seen_blank:
                line.strip().split('-')
                low, high = [int(x) for x in line.strip().split('-')]
                self.ranges.append( (low, high) )
            else:
                self.ingredients.append(int(line.strip()))

        self.rangelist = RangeList(self.ranges[0][0], self.ranges[0][1])
        for low, high in self.ranges[1:]:
            self.rangelist.add_range(low, high)          
        
    def part_one(self):
        fresh = 0
        for ingredient in self.ingredients:
            leaf, pos = self.rangelist.find_value(ingredient)
            if leaf is not None:
                fresh += 1
            
        return fresh

    def part_two(self):
        valid_ingredients = 0
        for leaf in self.rangelist.root:
            valid_ingredients += (leaf.high - leaf.low + 1)
        return valid_ingredients