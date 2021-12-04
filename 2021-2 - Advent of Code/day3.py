"""
Eric AKA Nyveon
https://adventofcode.com/2021/day/3
"""

# Imports
from collections import defaultdict

# -- Part 1 --

# Input
with open("day3.txt", 'r') as file:
    lines = file.readlines()
    diagnostics = [line.rstrip() for line in lines]
    input_size = len(diagnostics)
    line_length = len(diagnostics[0])
    diagnostics_copy = diagnostics.copy()

# Variables
set_bits = defaultdict(int)
gamma_rate = ""
epsilon_rate = ""

# Processing
for diagnostic in diagnostics:
    for index, character in enumerate(diagnostic):
        set_bits[index] += int(character)

for i in range(line_length):
    gamma_rate += '1' if set_bits[i] > input_size/2 else '0'
    epsilon_rate += '1' if set_bits[i] < input_size/2 else '0'

energy_rating = int(gamma_rate, 2) * int(epsilon_rate, 2)

# Output
print(f"What is the power consumption of the submarine? {energy_rating}")


# -- Part 2 --

# Variables
oxygen_rate = ""
scrubber_rate = ""


# Processing
def count_set_bits(_index, array):
    _set_bits = 0
    for _diagnostic in array:
        _set_bits += int(_diagnostic[_index])
    return _set_bits


for i in range(line_length):
    if len(diagnostics) != 1:
        if count_set_bits(i, diagnostics) >= len(diagnostics)/2:
            diagnostics = list(filter(lambda x: (x[i] == '1'), diagnostics))
        else:
            diagnostics = list(filter(lambda x: (x[i] == '0'), diagnostics))
    if len(diagnostics_copy) != 1:
        if count_set_bits(i, diagnostics_copy) < len(diagnostics_copy)/2:
            diagnostics_copy = list(filter(lambda x: (x[i] == '1'), diagnostics_copy))
        else:
            diagnostics_copy = list(filter(lambda x: (x[i] == '0'), diagnostics_copy))

life_rating = int(diagnostics[0], 2) * int(diagnostics_copy[0], 2)

# Output
print(f"What is the life support rating of the submarine? {life_rating}")
