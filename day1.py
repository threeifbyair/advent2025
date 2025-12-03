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
        zeros = 0
        current = 50
        for val in self.input:
            old_current = current
            extra_clicks = val[1] // 100
            if val[0] == 'L':
                current -= val[1] % 100
            elif val[0] == 'R':
                current += val[1] % 100
            if current >= 100:
                current -= 100
                if current != 0:
                    extra_clicks += 1
            if current < 0:
                current += 100
                if current != 0 and old_current != 0:
                    extra_clicks += 1
            if current == 0:
                extra_clicks += 1
            if self.args.verbose:
                print(f'Got instruction {val}, new value is {current}, clicks {extra_clicks}, zeros now {zeros + extra_clicks}')
            zeros += extra_clicks
        return zeros

