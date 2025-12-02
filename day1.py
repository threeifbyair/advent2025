#!/usr/bin/env python3

import re
import sys, os

import adventday

class Day1(adventday.AdventDay):
    def analyze_lines(self):
        self.input = [(x[0], int(x[1:])) for x in self.lines if len(x.strip()) > 0]
        
    def part_one(self):
        zeros = 0
        current = 50
        for val in self.input:
            if val[0] == 'L':
                current -= val[1] % 100
            elif val[0] == 'R':
                current += val[1] % 100
            if current >= 100:
                current -= 100
            if current < 0:
                current += 100
            if self.args.verbose:
                print(f'Got instruction {val}, new value is {current}{", new zero" if current == 0 else ""}')
            if current == 0:
                zeros += 1
        return zeros

    def part_two(self):
        name_ptr = 0
        for instr in self.instructions:
            if instr[0] == 'L':
                name_ptr = (name_ptr - int(instr[1:])) % len(self.dragon_names)
            elif instr[0] == 'R':
                name_ptr = (name_ptr + int(instr[1:])) % len(self.dragon_names)
        return self.dragon_names[name_ptr]
