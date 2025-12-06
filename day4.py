#!/usr/bin/env python3

import re
import sys, os

import adventday

class Day4(adventday.AdventDay):
    def analyze_lines(self):
        self.grid = []
        self.grid.append('.'*(len(self.lines[0].strip())+2))
        for line in self.lines:
            self.grid.append('.' + line.strip() + '.')
        self.grid.append('.'*(len(self.lines[0].strip())+2))
        
    def part_one(self):
        accessible = 0
        for y in range(1,len(self.grid)-1):
            for x in range(1, len(self.grid[y])-1):
                if self.grid[y][x] != '@':
                    continue
                neighbors = [self.grid[y-1][x-1], self.grid[y-1][x], self.grid[y-1][x+1],
                             self.grid[y  ][x-1],                    self.grid[y  ][x+1],
                             self.grid[y+1][x-1], self.grid[y+1][x], self.grid[y+1][x+1]]
                occupancylist = [1 if i == '@' else 0 for i in neighbors]
                occupancy = sum(occupancylist)
                if occupancy < 4:
                    accessible += 1
        return accessible

    def part_two(self):
        removed = 0
        while True:
            accessible = 0
            for y in range(1,len(self.grid)-1):
                for x in range(1, len(self.grid[y])-1):
                    if self.grid[y][x] != '@':
                        continue
                    neighbors = [self.grid[y-1][x-1], self.grid[y-1][x], self.grid[y-1][x+1],
                                self.grid[y  ][x-1],                    self.grid[y  ][x+1],
                                self.grid[y+1][x-1], self.grid[y+1][x], self.grid[y+1][x+1]]
                    occupancylist = [1 if i == '@' else 0 for i in neighbors]
                    occupancy = sum(occupancylist)
                    if occupancy < 4:
                        accessible += 1
                        self.grid[y] = self.grid[y][:x] + '.' + self.grid[y][x+1:]
            removed += accessible
            if accessible == 0:
                break
        return removed
