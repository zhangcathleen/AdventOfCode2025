#!/usr/bin/env python3

import sys
from collections import deque


# parse the puzzle list of strings
def parse_puzzle(content):
    dial = 50 # starting position of dial is 50
    sign = 1 # positive
    safe = deque(range(100)) # is a list [0 ... 99]
    safe.rotate(dial)
    password = 0

    for turn in content:
        line = turn.rstrip()

        if turn[0] == 'L':
            sign = 1
        elif turn[0] == "R":
            sign = -1
        
        str_num = line[1:]
        number = int(str_num) * sign
        safe.rotate(number) 
        dial = safe[0] # where the position of the dial is now
        
        if dial == 0:
            password += 1
    
    return password

# open puzzle input file and returns a list of the rotations
def open_puzzle(args):
    file = open(sys.argv[1], "r")
    content = file.readlines()
    file.close()
    return content

# take in the puzzle input file
def take_input():
    if len(sys.argv) == 1:
        print("add file with puzzle input please")
    else:
        content = open_puzzle(sys.argv)
        pwd = parse_puzzle(content)
        print(pwd)

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
