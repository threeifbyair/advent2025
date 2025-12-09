#!/usr/bin/env python3

import re
import sys
import argparse
import os
import random
import hashlib

import day1, day2, day3, day4, day5 #, day6, day7, day8, day9, day10, day11, day12

daylist = {
    1: day1.Day1,
    2: day2.Day2,
    3: day3.Day3,
    4: day4.Day4,
    5: day5.Day5,
    #6: day6.Day6,
    #7: day7.Day7,
    #8: day8.Day8,
    #9: day9.Day9,
    #10: day10.Day10,
    #11: day11.Day11,
    #12: day12.Day12,
}

def main(args):
    parser = argparse.ArgumentParser(description='Everybody Codes 2025')
    parser.add_argument('-i', '--input', type=str, help='Input file')
    parser.add_argument('-p', '--part-two', action='store_true', help='Perform part two of the challenge')
    parser.add_argument('-e', '--encrypted', action='store_true', help='Input is encrypted')
    parser.add_argument('-w', '--write', action='store_true', help='Write decrypted data to file and quit')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose output')
    parser.add_argument('-a', '--argint', type=int, help='An extra argument')
    parser.add_argument('-A', '--argint2', type=int, help='Another extra argument')
    parser.add_argument('day', type=int, nargs='*', help='Which day to run')
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f'File not found: {args.input}')
        return 1

    if args.encrypted:
        if 'AOC_PASSWORD' not in os.environ:
            print('AOC_PASSWORD environment variable not set for encrypted input')
            return 1
        password = os.environ['AOC_PASSWORD']
        # Create a hash of the password, seed a PRNG with it, and XOR that with the file contents
        with open(args.input, 'rb') as f:
            encrypted_data = f.read()
        hash_obj = hashlib.sha256(password.encode('utf-8'))
        seed = int.from_bytes(hash_obj.digest(), 'big')
        random.seed(seed)
        decrypted_data = bytearray()
        for byte in encrypted_data:
            decrypted_data.append(byte ^ random.randint(0, 255))
        if args.write:
            decrypted_filename = args.input + '.enc'
            with open(decrypted_filename, 'wb') as f:
                f.write(decrypted_data)
            if args.verbose:
                print(f'Wrote decrypted data to {decrypted_filename}')
            return 0
        lines = decrypted_data.decode('utf-8').splitlines()
    else:
        with open(args.input, 'r') as f:
            lines = [x.strip() for x in f.readlines()]

    if args.day:
        day = args.day[0]
    else:
        day = 1

    if day not in daylist:
        print(f'Invalid day: {day}')
        return 1

    result = daylist[day](lines, args)
    print(result.run())

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))