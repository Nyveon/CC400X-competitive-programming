"""
Eric AKA Nyveon
https://adventofcode.com/2021/day/2
"""

# -- Part 1 --

# Input
with open("day2.txt", 'r') as file:
    lines = file.readlines()
    instructions = [line.split() for line in lines]
    instructions = [(item[0], int(item[1])) for item in instructions]
    instructions_copy = instructions.copy()

# Variables
directions = {
    'forward': (1, 0),
    'down': (0, 1),
    'up': (0, -1)
}
position_horizontal = 0
position_vertical = 0

# Processing
for instruction in instructions:
    instruction_type, instruction_power = instruction
    position_horizontal += directions[instruction_type][0] * instruction_power
    position_vertical += directions[instruction_type][1] * instruction_power
multiplied_position = position_vertical * position_horizontal

# Output
print(f"What do you get if you multiply your final horizontal position by your final depth? {multiplied_position}")


# -- Part 2 --

# Variables
position_horizontal = 0
position_vertical = 0
position_aim = 0

# Processing
for instruction in instructions:
    instruction_type, instruction_power = instruction
    if instruction_type == 'down':
        position_aim += instruction_power
    elif instruction_type == 'up':
        position_aim -= instruction_power
    elif instruction_type == 'forward':
        position_horizontal += instruction_power
        position_vertical += position_aim * instruction_power
multiplied_position = position_vertical * position_horizontal

# Output
print(f"What do you get if you multiply your final horizontal position by your final depth? {multiplied_position}")