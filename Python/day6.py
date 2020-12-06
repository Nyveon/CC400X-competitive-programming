# Nyveon
# Advent of code 2020
# Day 5
# Python 3

# Input
file = open("day6_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()
file.close()
passes = file_in.split("\n\n")
passes2 = file_in.split("\n\n")


# -- Part 1 --
for i in range(len(passes)):
    passes[i] = passes[i].replace("\n", "")
    passes[i] = set(passes[i])

sum_part1 = 0
for i in passes:
    sum_part1 += len(i)

print("Part 1:", sum_part1)

# -- Part 2 --
sum_part2 = 0
for i in range(len(passes2)):
    passes2[i] = passes2[i].rstrip()
    passes2[i] = passes2[i].split("\n")
    for j in passes[i]:
        flag = True
        for k in passes2[i]:
            if j not in k:
                flag = False
        if flag:
            sum_part2 += 1

print("Part 2:", sum_part2)

