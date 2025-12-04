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

    def next_level(self, joltage, position, level, value):
        for highval in reversed(sorted(joltage.values.keys())):
            poslist = [x for x in joltage.values[highval] if x > position]
            if len(poslist) > 0:
                # We can use this!
                if level == 11:
                    # We're done!
                    return value * 10 + highval
                else:
                    newval = self.next_level(joltage, poslist[0], level+1, value*10+highval)
                    if newval is not None:
                        return newval
        # Looks like we didn't find anything.
        return None

    def part_two(self):
        power = 0
        for joltage in self.joltages:
            this_power = self.next_level(joltage, -1, 0, 0)
            if self.args.verbose:
                print(f'Got power {this_power}')
            power += this_power

        return power
