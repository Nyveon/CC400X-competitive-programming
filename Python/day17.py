# Nyveon
# Advent of code 2020
# Day 17
# Python 3

import numpy

# -- Input --
file = open("day17_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()[:-1]
file.close()
lines = file_in.split("\n")


# -- Part 1 --

# Generate space
input_height = len(lines)
input_width = len(lines[0])
max_distance = input_height + 12
size = (max_distance, max_distance, max_distance)
space = numpy.zeros(size)
center = max_distance//2

# Populate with input
for i in range(input_height):
    for j in range(input_width):
        if lines[i][j] == "#":
            space[center - (input_height//2 - i), center - (input_width//2 - j), center] = 1 #z = middle

# Counts state of 27 cells in a cube
def neighbors(a, x, y, z):
    counter = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                if max_distance > (x + i) > -1 and max_distance > (y + j) > -1 and max_distance > (z + k) > -1:
                    if a[x + i, y + j, z + k] == 1:
                        counter += 1
    return counter # -1 if center is #

# Cycles the space
def cycle(a):
    next = a.copy()
    for x in range(max_distance):
        for y in range(max_distance):
            for z in range(max_distance):
                n = neighbors(a, x, y, z)
                if a[x, y, z] == 1:
                    n -= 1
                    if not (n == 2 or n == 3):
                        next[x, y, z] = 0
                elif a[x, y, z] == 0:
                    if n == 3:
                        next[x, y, z] = 1
    return next

# Debug function for dsiplaying a slice of space
def show_slice(z):
    print("z =", z)
    for x in range(max_distance):
        for y in range(max_distance):
            if space[x, y, z] == 0:
                print("█", end=" ")
            else:
                print("#", end=" ")
        print("")
    print("---")

# Counts active cells in a space
def count_active(a):
    counter = 0
    for x in range(max_distance):
        for y in range(max_distance):
            for z in range(max_distance):
                if a[x, y, z] == 1:
                    counter += 1
    return counter

for i in range(6):
    print("Progress:", i, "/ 6")
    space = cycle(space)

print("Part 1: ", count_active(space))


# -- Part 2 --

# Generate space
input_height = len(lines)
input_width = len(lines[0])
max_distance =input_height + 13
size = (max_distance, max_distance, max_distance, max_distance)
space = numpy.zeros(size)
center = max_distance//2

# Populate with input
for i in range(input_height):
    for j in range(input_width):
        if lines[i][j] == "#":
            space[center - (input_height//2 - i), center - (input_width//2 - j), center, center] = 1

# Counts state of 81 cells in a hypercube
def neighbors_4d(a, x, y, z, w):
    counter = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if max_distance > (x + i) > -1 and max_distance > (y + j) > -1 and max_distance > (z + k) > -1 and max_distance > (w + l) > -1:
                        if a[x + i, y + j, z + k, w + l] == 1:
                            counter += 1
                            if counter > 4: # optimization
                                return counter
    return counter # -1 if center is #

# Cycles the space
def cycle_4d(a):
    next = a.copy()
    for x in range(max_distance):
        for y in range(max_distance):
            for z in range(max_distance):
                for w in range(max_distance):
                    n = neighbors_4d(a, x, y, z, w)
                    if a[x, y, z, w] == 1:
                        n -= 1
                        if not (n == 2 or n == 3):
                            next[x, y, z, w] = 0
                    elif a[x, y, z, w] == 0:
                        if n == 3:
                            next[x, y, z, w] = 1
    return next

# Counts active cells in a space
def count_active_4d(a):
    counter = 0
    for x in range(max_distance):
        for y in range(max_distance):
            for z in range(max_distance):
                for w in range(max_distance):
                    if a[x, y, z, w] == 1:
                        counter += 1
    return counter

for i in range(6):
    print("Progress:", i, "/ 6")
    space = cycle_4d(space)

print("Part 2: ", count_active_4d(space))