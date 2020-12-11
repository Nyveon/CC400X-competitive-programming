# Nyveon
# Advent of code 2020
# Day 11
# Python 3


# -- Input --
file = open("day11_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()
file.close()
lines = file_in.split("\n")
lines.pop()

# -- Main functions --

# Debug function for rendering the map of cells.
def display(lines, a, b, a1, b1):
    print("------------------")
    for y in range(len(lines)):
        line = ""
        for x in range(len(lines[y])):
            if x == a and y == b:
                line += "O"
            elif x == a1 and y == b1:
                line += "X"
            else:
                line += lines[y][x]
        print(line)
    print("------------------")

# Function for looking in a direction of the map of cells.
def look(lines, x_dir, y_dir, x, y, distance):
    #print("Xd", x_dir, "Yd", y_dir)
    a1 = x
    b1 = y
    c = d = 0
    n = len(lines[y])
    m = len(lines)
    x += x_dir
    y += y_dir
    while (n > x > -1) and (m > y > -1) and (d < distance):
        #display(lines, x, y, a1, b1)
        if lines[y][x] == "#":
            c = 1
            break
        if lines[y][x] == "L":
            break
        x += x_dir
        y += y_dir
        d += 1
    return c

# Main function, simulates one cycle of the cells.
def cycle(lines, distance, tolerance):
    new_lines = []
    for y in range(len(lines)):
        line = ""
        for x in range(len(lines[y])):
            if lines[y][x] == "L":
                n = look(lines, 0, -1, x, y, distance)
                s = look(lines, 0, 1, x, y, distance)
                e = look(lines, -1, 0, x, y, distance)
                w = look(lines, 1, 0, x, y, distance)
                ne = look(lines, -1, -1, x, y, distance)
                nw = look(lines, 1, -1, x, y, distance)
                se = look(lines, 1, 1, x, y, distance)
                sw = look(lines, -1, 1, x, y, distance)

                if (n + s + e + w + nw + ne + sw + se) == 0:
                    line = line + "#"
                else:
                    line = line + lines[y][x]

            elif lines[y][x] == "#":
                n = look(lines, 0, -1, x, y, distance)
                s = look(lines, 0, 1, x, y, distance)
                e = look(lines, -1, 0, x, y, distance)
                w = look(lines, 1, 0, x, y, distance)
                ne = look(lines, -1, -1, x, y, distance)
                nw = look(lines, 1, -1, x, y, distance)
                se = look(lines, 1, 1, x, y, distance)
                sw = look(lines, -1, 1, x, y, distance)

                if (n + s + e + w + nw + ne + sw + se) >= tolerance:
                    line = line + "L"
                else:
                    line = line + lines[y][x]

            else:
                line = line + lines[y][x]

        new_lines.append(line)
    return new_lines

# -- Part 1 --

lines_1 = lines.copy()
while True:
    lines_step = cycle(lines_1, 1, 4)
    if lines_1 == lines_step:
        break
    lines_1 = lines_step

c = 0
for y in lines_1:
    c += y.count("#")

print("Part 1:", c)


# -- Part 2 --

lines_2 = lines.copy()
n = max(len(lines_2), len(lines_2[0]))
while True:
    lines_step = cycle(lines_2, n, 5)
    if lines_2 == lines_step:
        break
    lines_2 = lines_step

c = 0
for y in lines_2:
    c += y.count("#")

print("Part 2:", c)
