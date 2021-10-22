# Nyveon
# Advent of code 2020
# Day 13
# Python 3

# -- Input --
file = open("day13_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()
file.close()
lines = file_in.split("\n")
lines.pop()


# -- Part 1 --

# Input parsing
ingress = int(lines[0])
busses_pre = lines[1].split(",")
busses = []
for i in busses_pre:
    if i != "x":
        busses.append(int(i))
print(busses)


def min_index(a):
    m = 0
    for i in range(1, len(a)):
        if a[i] < a[m]:
            m = i
    return m

differences = []
for i in busses:
    x = i
    while x < ingress:
        x += i
    differences.append(x - ingress)

ans = min_index(differences)
print("Part 1:", busses[ans] * differences[ans])


# -- Part 2 --

# Input parsing
# wowee i'm coming back to this later :S