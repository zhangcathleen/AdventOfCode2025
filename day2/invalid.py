#!/usr/bin/env python3

import sys

# split the string of product ID ranges
# put them into a list of tuples
def split_ranges(s):
    ranges = s.split(",") # ranges is a list of strings

    for r in ranges:
        r.split()
    

# open puzzle input file and returns a list of the rotations
def open_puzzle(args):
    file = open(sys.argv[1], "r")
    content = file.readline()
    file.close()
    return content

# take in the puzzle input file
def take_input():
    if len(sys.argv) == 1:
        print("add file with puzzle input please")
    else :
        content = open_puzzle(sys.argv)
        split_ranges(content)

take_input()
print("hello world ~")

'''
    11-22 has two invalid IDs, 11 and 22.
    95-115 has one invalid ID, 99.
    998-1012 has one invalid ID, 1010.
    1188511880-1188511890 has one invalid ID, 1188511885.
    222220-222224 has one invalid ID, 222222.
    1698522-1698528 contains no invalid IDs.
    446443-446449 has one invalid ID, 446446.
    38593856-38593862 has one invalid ID, 38593859.
    The rest of the ranges contain no invalid IDs.

Adding up all the invalid IDs in this example produces 1227775554.
'''