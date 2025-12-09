#!/usr/bin/env python3

import re
import sys, os

import adventday

class Day6(adventday.AdventDay):
    def analyze_lines(self):
        self.values = []
        for line in self.lines:
            if '*' in line or '+' in line:
                self.operations = [x.strip() for x in line.split()]
            else:
                self.values.append([int(x) for x in line.strip().split()])

    def part_one(self):
        total = 0
        for pos, op in enumerate(self.operations):
            if op == '*':
                thistotal = 1
                for value in self.values:
                    thistotal *= value[pos]
                total += thistotal
            elif op == '+':
                thistotal = 0
                for value in self.values:
                    thistotal += value[pos]
                total += thistotal
        return total

    def part_two(self):
        return 0