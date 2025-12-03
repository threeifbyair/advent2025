#!/usr/bin/env python3

import re
import sys, os

import adventday

class Day2(adventday.AdventDay):
    def analyze_lines(self):
        ranges = self.lines[0].strip().split(',')
        self.input = []
        for r in ranges:
            splitrange = r.split('-')
            self.input.append((int(splitrange[0]), len(splitrange[0]), int(splitrange[1]), len(splitrange[1])))
        
    def part_one(self):
        invalids = 0
        for (low, lowlen, high, highlen) in self.input:
            # You can't have repeated patterns if the number of digits is odd
            if lowlen % 2 == 1:
                low = 10 ** lowlen
                lowlen += 1
            if highlen % 2 == 1:
                highlen -= 1
                high = 10 ** highlen - 1
            if high < low:
                continue

            assert lowlen == highlen
            # Now let's look at the possible invalids in the range.
            these_invalids = []
            # First, is low-repeated in the range?
            halfdigitlow = low // (10**(lowlen//2))
            firstrepeat = halfdigitlow * (10**(lowlen//2)) + halfdigitlow
            if firstrepeat >= low and firstrepeat <= high:
                these_invalids.append(firstrepeat)
            # First, is high-repeated in the range?
            halfdigithigh = high // (10**(highlen//2))
            lastrepeat = halfdigithigh * (10**(highlen//2)) + halfdigithigh
            if lastrepeat <= high and lastrepeat >= low and lastrepeat != firstrepeat:
                these_invalids.append(lastrepeat)
            # And all the numbers in between.
            if halfdigitlow != halfdigithigh:
                # Total should be 1/2n(n+1) * 1001 + lowval, roughly speaking
                for val in range(halfdigitlow+1, halfdigithigh):
                    thisval = val * (1 + (10**(lowlen//2)))
                    these_invalids.append(thisval)
            if self.args.verbose:
                print(f'From {low} to {high} the invalid IDs are: {these_invalids} summing to {sum(these_invalids)}')
            invalids += sum(these_invalids)
        return invalids

    def part_two(self):
        return 0
