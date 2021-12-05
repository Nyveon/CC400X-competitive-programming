"""
Eric AKA Nyveon
https://adventofcode.com/2021/day/5
"""

# -- Part 1

# Input
with open("day5.txt", 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

thermo = []
size_x = 0
size_y = 0
for line in lines:
    a, b = line.split("->")
    a1, a2 = a.split(",")
    b1, b2 = b.split(",")
    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)

    if a1 > size_x:
        size_x = a1
    if b1 > size_x:
        size_x = b1
    if a2 > size_y:
        size_y = a2
    if b2 > size_y:
        size_y = b2

    thermo.append(((a1, a2, b1, b2)))

size_x += 1
size_y += 1


# Variables
diagram = [[0 for _ in range(size_x)] for __ in range(size_y)]
count = 0


# Processing
for t in thermo:
    if t[0] == t[2]:
        start = min(t[1], t[3])
        stop = max(t[1], t[3])

        for y in range(start, stop+1):
            diagram[y][t[0]] += 1
    elif t[1] == t[3]:
        start = min(t[0], t[2])
        stop = max(t[0], t[2])

        for x in range(start, stop+1):
            diagram[t[1]][x] += 1


for row in diagram:
    for item in row:
        if item >= 2:
            count += 1

# Output
print(f"At how many points do at least two lines overlap? {count}")


# -- Part 2

# Variables
count = 0

# Processing
for t in thermo:
    if (t[0] != t[2]) and (t[1] != t[3]):
        if t[2] > t[0]:
            x_direction = 1
        else:
            x_direction = -1

        if t[3] > t[1]:
            y_direction = 1
        else:
            y_direction = -1

        distance = abs(t[2] - t[0])

        x = t[0]
        y = t[1]

        for i in range(distance+1):
            diagram[y][x] += 1
            x += x_direction
            y += y_direction

# Output

for row in diagram:
    for item in row:
        if item >= 2:
            count += 1


print(f"At how many points do at least two lines overlap? {count}")

