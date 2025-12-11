#!/usr/bin/env python3

import sys
from collections import deque


# parse the puzzle list of strings
def parse_puzzle(content):
    safe = deque(range(100)) # is a list [0 ... 99]
    dial = 50 # starting position of dial is 50
    safe.rotate(dial)   # rotate positively decreases numbers - left
                        # rotate negatively increases numbers - right

    left = True # right = False || sign = -1
    password = 0

    for turn in content:
        print(f"beginning of loop. dial is at {dial}")
        line = turn.rstrip()
        print(f"{line}")

        str_num = line[1:]
        num = int(str_num)

        rotations, number = divmod(num, 100)

        password += rotations

        if line[0] == 'L': # towards lower numbers - positive
            left = True
            safe.rotate(number)
        elif line[0] == "R": # towards higher numbers - negative
            left = False
            safe.rotate(number * -1)
        print(f"the safe is at {safe[0]}")

        if safe[0] == 0:
            password += 1
            print(f"dial is pointed at 0 {safe[0]}")
        elif dial != 0:
            if dial - number < 0 and left:
                password += 1
                print(f"left turn pointed at 0 : {dial} - {number} = {dial-number}")
            elif dial + number > 99 and not left :
                password += 1
                print(f"right turn pointed at 0 : {dial} + {number} = {dial+number}")
        
        dial = safe[0] # where the position of the dial is now
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