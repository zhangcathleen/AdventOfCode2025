#!/usr/bin/env python3

import sys


# returns true if given number is a sequence of digits repeated twice
def is_repeated(c):
    
    c_str = str(c)
    c_len = len(c_str)
    c_half = int(c_len / 2)

    first_half = c_str[ 0 : c_half ]
    second_half = c_str[ c_half : c_len ]
    return first_half == second_half
    



# find invalid ids from list of tuples
# invalid id = sequence of digits repeated twice
def find_repeats(ids):
    repeated = []

    for id in ids:
        first = id[0]
        last = id[1]
        counter = first

        while counter <= last:
            if is_repeated(counter):
                repeated.append(counter)
            counter += 1

    return repeated


# split the string of product ID ranges
# put them into a list of integer tuples
def split_ranges(s):
    ranges = s.split(",") # ranges is a list of strings
    ids = []

    for r in ranges:
        range = r.split("-")
        tuple_range = ()

        for item in range:
            num_item = int(item)
            a = (num_item,)
            tuple_range = tuple_range + a

        ids.append(tuple_range)

    return ids
    

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
        ids = split_ranges(content)
        repeated = find_repeats(ids)
        print(sum(repeated))

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