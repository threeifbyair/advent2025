#!/usr/bin/env python3

class AdventDay:
    def __init__(self, lines, args):
        self.lines = lines
        self.args = args

    def part_one(self):
        return 'Part one not implemented'

    def part_two(self):
        return 'Part two not implemented'

    def analyze_lines(self):
        pass

    def run(self):
        self.analyze_lines()
        if self.args.part_two:
            return self.part_two()
        return self.part_one()