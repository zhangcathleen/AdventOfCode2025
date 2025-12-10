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
        elif turn[0] == "R": # towards higher numbers - negative
            sign = -1
        
        str_num = line[1:]
        number = int(str_num)
        # print(f"at {dial} turn {number} * {sign}")

        # 0x434C49434B method ( click in hex )
        if dial != 0:
            if sign == 1: # if turning left
                if dial - number < 0 : # going negative passes 0
                    password += 1
                    print(f"turned left {number}, passed 0")
            elif sign == -1: # if turning right
                if dial + number > 99: # passes 0
                    password += 1
                    print(f"turned right {number}, passed 0")
        else:
            password += 1

        safe.rotate(number * sign) 
        dial = safe[0] # where the position of the dial is now
        
        # if dial == 0:
        #     password += 1
    
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
