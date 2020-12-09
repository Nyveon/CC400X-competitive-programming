# Nyveon
# Advent of code 2020
# Day 9
# Python 3

# -- Input --
file = open("day9_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()
file.close()
lines = file_in.split("\n")
lines.pop()
lines = [int(i) for i in lines]

# -- Part 1 --

def checker(lines, long, i):
    for j in range(long):
        for k in range(long):
            if lines[i] == lines[i-j - 1] + lines[i-k - 1]:
                return True
    return False

long = 25
for i in range(long, len(lines)):
    if not checker(lines, long, i):
        a = lines[i]
        break

print("Part 1:", a)

# -- Part 2 --

def summer(lines, large, target):
    for i in range(0, len(lines)-large + 1):
        sum = 0
        for j in range(0, large):
            sum += lines[j + i]
        if sum == target:
            return (True, i)

    return (False, 0)

for large in range(2, len(lines)):
    ans = summer(lines, large, a)
    if ans[0]:
        ans_list = []
        for j in range(0, large):
            ans_list.append(lines[j + ans[1]])
        print("Part 2:", max(ans_list) + min(ans_list))
        break


