# Nyveon
# Advent of code 2020
# Day 12
# Python 3

import math

# -- Input --
file = open("day12_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()
file.close()
lines = file_in.split("\n")
lines.pop()


# -- Part 1 --
directions = {"N" : [1, 0], "S" : [-1, 0], "E" : [0, 1], "W" : [0, -1], }
direction = 0
x = 0
y = 0

for i in range(len(lines)):
    instruction = lines[i][0]
    number = int(lines[i][1:])

    if instruction == "L":
        direction = (direction + number) % 360
    elif instruction == "R":
        direction = (direction - number) % 360
    elif instruction == "F":
        x += math.cos(math.radians(direction)) * number
        y += math.sin(math.radians(direction)) * number
    else:
        x += directions[instruction][1] * number
        y += directions[instruction][0] * number

print("Part 1:", abs(x) + abs(y))


# -- Part 2 --
w_x = 10
w_y = 1
x = 0
y = 0

for i in range(len(lines)):
    instruction = lines[i][0]
    number = int(lines[i][1:])

    if instruction == "L":
        w_xo = w_x
        w_x = w_x * math.cos(math.radians(number)) - w_y * math.sin(math.radians(number))
        w_y = w_y * math.cos(math.radians(number)) + w_xo * math.sin(math.radians(number))
    elif instruction == "R":
        w_xo = w_x
        w_x = w_x * math.cos(math.radians(-number)) - w_y * math.sin(math.radians(-number))
        w_y = w_y * math.cos(math.radians(-number)) + w_xo * math.sin(math.radians(-number))
    elif instruction == "F":
        x += w_x * number
        y += w_y * number
    else:
        w_x += directions[instruction][1] * number
        w_y += directions[instruction][0] * number

print("Part 2:", abs(x) + abs(y))