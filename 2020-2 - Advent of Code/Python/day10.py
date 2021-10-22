# Nyveon
# Advent of code 2020
# Day 10
# Python 3



# -- Input --
file = open("day10_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()
file.close()
lines = file_in.split("\n")
lines.pop()
lines = [int(i) for i in lines]

# -- Part 1 --
lines.append(0)
lines.sort()
differences = []
for i in range(1, len(lines)):
    d = lines[i] - lines[i - 1]
    differences.append(d)

print("Part 1:", (differences.count(3) + 1) * differences.count(1))

# -- Part 2 --
switchables = 1
magic = [0, 2, 4, 7, 13, 24, 44] # This may look bad but it's really just a modified tribonacci
differences.append(3)
count = 0

for i in range(len(differences)-1):
    if count == 0:
        if differences[i] == 1 and differences[i + 1] == 1:
            count += 1
    else:
        if differences[i] == 1 and differences[i + 1] == 1:
            count += 1
        else:
            switchables *= magic[count]
            count = 0
print("Part 2:", switchables)


