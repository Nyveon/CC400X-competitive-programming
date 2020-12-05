# Nyveon
# Advent of code 2020
# Day 5
# Python 3

# Input
file = open("day5_input.txt", "r")
file_in = file.read()
file.close()
passes = file_in.split("\n")


# -- Part 1 --
pass_id = []
line = 0
for item in passes:
    item = item.replace("F", "0")
    item = item.replace("B", "1")
    item = item.replace("L", "0")
    item = item.replace("R", "1")
    pass_id.append(int(item[0:7], 2)*8 + int(item[7:10], 2))

# Output
print("Part 1:", max(pass_id))


# -- Part 2 --
pass_id.sort()
for i in range(len(pass_id)-1):
    if (pass_id[i + 1] - pass_id[i] != 1):
        print("Part 2:", pass_id[i] + 1) # Output
