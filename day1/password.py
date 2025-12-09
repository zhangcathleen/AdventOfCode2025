#!/usr/bin/env python3

import sys


# parse the puzzle input file strings
def parse_puzzle(content):
    dial = 50
    for char in content:
        rep = repr(char)
        print(rep)
'''        if rep == "L":
            # TODO negative
        elif rep == "R":
            # TODO positive
        elif rep == "'\n'":
            # TODO next rotation string of numbers to integers
        else:
            # TODO numbers add to a string of numbers
'''
# open puzzle input file
def open_puzzle(args):
    file = open(sys.argv[1], "r")
    content = file.read()
    file.close()
    return content

# take in the puzzle input file
def take_input():
    if len(sys.argv) == 1:
        print("add file with puzzle input please")
    else:
        content = open_puzzle(sys.argv)
        parse_puzzle(content)

take_input()
print("hello world")


'''
Dial 0 - 99 :
    ... 95 96 97 98 99 0 1 2 3 ...

Dial starts at 50

Ex : 
    Dial at 5 ( D5 ) + Rotation of L10 ( L10 ) = D95
    D95 + R5 = D0

Password = number of times dial is at D0 after any rotation in the sequence

Test :

L68
L30
R48
L5
R60
L55
L1
L99
R14
L82

    Password = 3

'''
