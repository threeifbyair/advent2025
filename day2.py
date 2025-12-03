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
        invalids = []
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
                print(f'From {low} to {high} the invalid IDs are: {these_invalids} summing to ')
            invalids += these_invalids
        return sum(set(invalids))

    def repeat_number(self, number, numberlen, split):
        answer = 0
        for i in range(split):
            answer += number * (10**(numberlen*i))
        return answer

    def find_split_invalids(self, low, high, numberlen, split):
        # We know here that we can split this number into this many pieces. So let's do it.
        these_invalids = []
        smallerlen = numberlen // split
        halfdigitlow = low // (10**(smallerlen * (split-1)))
        halfdigithigh = high // (10**(smallerlen * (split-1)))
        firstrepeat = self.repeat_number(halfdigitlow, smallerlen, split)
        if firstrepeat >= low and firstrepeat <= high:
            these_invalids.append(firstrepeat)
        lastrepeat = self.repeat_number(halfdigithigh, smallerlen, split)
        if lastrepeat <= high and lastrepeat >= low and lastrepeat != firstrepeat:
            these_invalids.append(lastrepeat)
        # And all the numbers in between.
        if halfdigitlow != halfdigithigh:
            # Total should be 1/2n(n+1) * 1001 + lowval, roughly speaking
            for val in range(halfdigitlow+1, halfdigithigh):
                thisval = self.repeat_number(val, smallerlen, split)
                these_invalids.append(thisval)
        if self.args.verbose:
            print(f'From {low} to {high} split by {split} the invalid IDs are: {these_invalids}')
        return these_invalids


    def find_invalids(self, low, high, numberlen):
        # How many pieces can we break a number into?
        invalids = []
        for split in range(2, numberlen+1):
            if numberlen % split == 0:
                invalids += self.find_split_invalids(low, high, numberlen, split)
        return invalids

    def part_two(self):
        invalids = []
        for (low, lowlen, high, highlen) in self.input:
            # First break up pieces of different lengths.
            if lowlen != highlen:
                assert highlen == lowlen + 1
                invalids += self.find_invalids(low, 10**(highlen-1)-1, lowlen)
                invalids += self.find_invalids(10**(highlen-1), high, highlen)
            else:
                invalids += self.find_invalids(low, high, highlen)

        return sum(set(invalids))
