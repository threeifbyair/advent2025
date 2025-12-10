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
        tachyons = {self.values[1].index('S'): 1}
        for line in self.values[2:]:
            new_tachyons = {}
            for pos in tachyons:
                if line[pos] == '^':
                    if pos-1 not in new_tachyons:
                        new_tachyons[pos-1] = 0
                    new_tachyons[pos-1] += tachyons[pos]
                    if pos+1 not in new_tachyons:
                        new_tachyons[pos+1] = 0
                    new_tachyons[pos+1] += tachyons[pos]
                else:
                    if pos not in new_tachyons:
                        new_tachyons[pos] = 0
                    new_tachyons[pos] += tachyons[pos]
            tachyons = new_tachyons
        return sum(tachyons.values())
