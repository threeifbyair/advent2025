#!/usr/bin/env python3

import re
import sys, os

import adventday

class Day9(adventday.AdventDay):
    def analyze_lines(self):
        self.num_closest = self.args.argint if self.args.argint else 1000
        self.points = []
        for line in self.lines:
            self.points.append([int(x) for x in line.strip().split(',')])

    def process_points(self, is_part_two=False):
        self.areas = {}
        for i, point in enumerate(self.points):
            for j, otherpoint in enumerate(self.points[i+1:], start=i+1):
                area = (abs(otherpoint[0]-point[0]) + 1) * (abs(otherpoint[1]-point[1]) + 1)
                if self.args.verbose: 
                    print(f'Area between point {i} {point} and point {j} {otherpoint} is {area}')
                if area not in self.areas:
                    self.areas[area] = []
                self.areas[area].append( (i, j) )

        sorted_areas = sorted(self.areas.keys())
        return sorted_areas[-1]

    def part_one(self):
        return self.process_points(is_part_two=False)

    def part_two(self):
        return self.process_points(is_part_two=True)

