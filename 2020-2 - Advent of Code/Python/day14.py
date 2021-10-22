# Nyveon
# Advent of code 2020
# Day 14
# Python 3

# -- Input --
file = open("day14_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()
file.close()
lines = file_in.split("\n")
lines.pop()

# -- Part 1 --
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
memory = {}
for line in lines:
    if line[:2] == "ma":
        # Reset mask
        mask = line[7:]
    else:
        # Separate input
        line = line.split("=")
        slot = int(line[0][4:-2])
        value = list(bin(int(line[1][1:]))[2:])

        # Add trailing zeroes to value
        while len(value) < 36:
            value.insert(0, 0)

        # Apply mask
        for i in range(len(mask)):
            if mask[i] != "X":
                value[i] = mask[i]

        # Add value as integer to memory slot
        memory[slot] = int(''.join([str(i) for i in value]), 2)

sum = 0
for key in memory:
    sum += memory[key]
print("Part 1:", sum)



# -- Part 2 --


mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
memory = {}
for line in lines:
    if line[:2] == "ma":
        # Reset mask
        mask = line[7:]
    else:
        # Separate input
        line = line.split("=")
        slot = list(bin(int(line[0][4:-2]))[2:])
        value = int(line[1][1:])

        # Add trailing zeroes to slot
        while len(slot) < 36:
            slot.insert(0, 0)

        # Apply mask
        for i in range(len(mask)):
            if mask[i] != "0":
                slot[i] = mask[i]

        # Permutations
        adresses = []
        size = slot.count("X")
        for i in range(2**size):
            current = slot.copy()
            permutation = str(bin(i)[2:])
            while len(permutation) < size:
                permutation = "0" + permutation
            counter = 0
            for j in range(len(current)):
                if current[j] == "X":
                    current[j] = permutation[counter]
                    counter += 1
            adresses.append(current)

        # Update memory
        for adress in adresses:
            memory[int(''.join([str(i) for i in adress]), 2)] = value

sum = 0
for key in memory:
    sum += memory[key]
print("Part 2:", sum)
