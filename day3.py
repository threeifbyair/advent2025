#!/usr/bin/env python3

import re
import sys, os

import adventday

class Joltage:
    def __init__(self, line):
        self.line = [int(x) for x in line]
        self.values = {}
        for pos, val in enumerate(self.line):
            if val not in self.values:
                self.values[val] = []
            self.values[val].append(pos)

class Day3(adventday.AdventDay):
    def analyze_lines(self):
        self.joltages = []
        for line in self.lines:
            self.joltages.append(Joltage(line))
            
        
    def part_one(self):
        power = 0
        for joltage in self.joltages:
            this_power = 0
            for highval in reversed(sorted(joltage.values.keys())):
                firstpos = joltage.values[highval][0]
                for lowval in reversed(sorted(joltage.values.keys())):
                    if joltage.values[lowval][-1] > firstpos:
                        # We got one!
                        this_power = highval * 10 + lowval
                        break
                if this_power != 0:
                    break
            if self.args.verbose:
                print(f'Got power {this_power} from locations {joltage.values[highval][0]} and {joltage.values[lowval][-1]}')
            power += this_power

        return power

    def part_two(self):
        return 0
