# Nyveon
# Advent of code 2020
# Day 15
# Python 3


# -- Input --
file = open("day15_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()[:-1]
file.close()
lines = file_in.split(",")
for i in range(len(lines)):
    lines[i] = int(lines[i])


# -- Part 1 --

# Input numbers
memory = {}
turn = 0
for i in lines:
    turn += 1
    memory[i] = [turn, 0]
last_spoken = lines[len(lines) - 1]

# Play the game
while turn < 2020:
    turn += 1
    value = memory[last_spoken]
    if value[1] == 0:
        last_spoken = 0
    else:
        last_spoken = value[0] - value[1]
    if last_spoken not in memory:
        memory[last_spoken] = [turn, 0]
    memory[last_spoken][1] = memory[last_spoken][0]
    memory[last_spoken][0] = turn
print("Part 1:", last_spoken)


# -- Part 2 --
# Input numbers
memory = {}
turn = 0
for i in lines:
    turn += 1
    memory[i] = [turn, 0]
last_spoken = lines[len(lines) - 1]

# Play the game
while turn < 30000000:
    turn += 1
    value = memory[last_spoken]
    if value[1] == 0:
        last_spoken = 0
    else:
        last_spoken = value[0] - value[1]
    if last_spoken not in memory:
        memory[last_spoken] = [turn, 0]
    memory[last_spoken][1] = memory[last_spoken][0]
    memory[last_spoken][0] = turn
print("Part 2:", last_spoken)




