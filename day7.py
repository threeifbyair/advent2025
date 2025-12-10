#!/usr/bin/env python3

import re
import sys, os

import adventday

class Day7(adventday.AdventDay):
    def analyze_lines(self):
        self.values = [''.join(['.'] * (len(self.lines[0].strip()) + 2))] + ['.' + x + '.' for x in self.lines] + [''.join(['.'] * (len(self.lines[0].strip()) + 2))]

    def part_one(self):
        splits = 0
        tachyons = set((self.values[1].index('S'),))
        for line in self.values[2:]:
            new_tachyons = set()
            for pos in tachyons:
                if line[pos] == '^':
                    new_tachyons.add(pos-1)
                    new_tachyons.add(pos+1)
                    splits += 1
                else:
                    new_tachyons.add(pos)
            tachyons = new_tachyons
        return splits             

    def part_two(self):
        # We need to re-interpret the lines...
        spacelist = []
        for line in self.lines[:-1]:
            thesespaces = set()
            for pos, ch in enumerate(line):
                if ch == ' ':
                    thesespaces.add(pos)
            spacelist.append(thesespaces)
        commonspaces = set.intersection(*spacelist)
        breaks = [-1] + sorted(list(commonspaces)) + [max(len(x) for x in self.lines[:-1])]
        # Now re-parse the values based on these common spaces
        total = 0
        for i in range(len(breaks)-1):
            values = [0] * (breaks[i+1]-breaks[i]-1)
            for j in range(breaks[i]+1, breaks[i+1]):
                for k in self.lines[:-1]:
                    if j < len(k) and k[j] != ' ':
                        values[j-breaks[i]-1] *= 10
                        values[j-breaks[i]-1] += int(k[j])
                if j < len(self.lines[-1]) and self.lines[-1][j] in ('*', '+'):
                    operation = self.lines[-1][j]
            if operation == '*':
                thistotal = 1
                for value in values:
                    thistotal *= value
                total += thistotal
            elif operation == '+':
                thistotal = 0
                for value in values:
                    thistotal += value
                total += thistotal
        return total
