#!/usr/bin/env python3

import sys
from collections import deque


# parse the puzzle list of strings
def parse_puzzle(content):
    safe = deque(range(100)) # is a list [0 ... 99]

    dial = 50 # starting position of dial is 50
    safe.rotate(dial) 
    # rotate positively decreases numbers - left
    # rotate negatively increases numbers - right

    sign = -1
    password = 0

    for turn in content:
        line = turn.rstrip()

        if turn[0] == 'L': # towards lower numbers - positive
            sign = 1
            print("left")
        elif turn[0] == "R": # towards higher numbers - negative
            sign = -1
            print("right")
        
        str_num = line[1:]
        number = int(str_num) * sign
        print(number)

        # TODO can't figure out how to calculate when the dial points at zero
        # if dial - number < -1 :
        #     password += 1
        #     print("once less than 0")
        # elif dial - number > 100 :
        #     password += 1
        #     print("once greater than 100")

        safe.rotate(number) 
        dial = safe[0] # where the position of the dial is now
        
        # print(f"turn {number} clicks to get to {dial}")

        if dial == 0:
            password += 1
            print("dial at zero")
    
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
