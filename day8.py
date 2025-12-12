#!/usr/bin/env python3

import re
import sys, os

import adventday

class Day8(adventday.AdventDay):
    def analyze_lines(self):
        self.num_closest = self.args.argint if self.args.argint else 1000
        self.points = []
        for line in self.lines:
            self.points.append([int(x) for x in line.strip().split(',')])

    def part_one(self):
        self.distances = {}
        for i, point in enumerate(self.points):
            for j, otherpoint in enumerate(self.points[i+1:], start=i+1):
                distance = (otherpoint[0]-point[0])**2 + (otherpoint[1]-point[1])**2 + (otherpoint[2]-point[2])**2
                if distance not in self.distances:
                    self.distances[distance] = []
                self.distances[distance].append( (i, j) )

        self.groups = {i: set([i]) for i in range(len(self.points))}

        sorted_distances = sorted(self.distances.keys())
        num_pairs_used = 0
        for distance in sorted_distances:
            pairs = self.distances[distance]
            if self.args.verbose:
                print(f'Distance {distance} has {len(pairs)} pairs: {pairs}')
                print(f'Groups before processing: {self.groups}')
                groups2 = set([frozenset(x) for x in self.groups.values()])
                print(f'Unique groups: {groups2}')
            for pair in pairs:
                group1 = self.groups[pair[0]]
                group2 = self.groups[pair[1]]
                if self.args.verbose:
                    print(f'Processing pair #{num_pairs_used+1}: {pair}, groups {group1} and {group2}')
                if group1 is group2:
                    num_pairs_used += 1
                    if num_pairs_used >= self.num_closest:
                        break
                    continue
                # Merge groups.
                group1.update(group2)
                for member in group2:
                    self.groups[member] = group1
                num_pairs_used += 1
                if num_pairs_used >= self.num_closest:
                    break
            if num_pairs_used >= self.num_closest:
                break

        biggest_groups = sorted(len(x) for x in set([frozenset(x) for x in self.groups.values()]))  

        return biggest_groups[-1] * biggest_groups[-2] * biggest_groups[-3]

    def part_two(self):
        return 0