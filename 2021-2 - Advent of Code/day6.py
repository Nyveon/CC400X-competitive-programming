"""
Eric AKA Nyveon
https://adventofcode.com/2021/day/6
"""

# -- Part 1 --

# Input
with open("day6.txt", 'r') as file:
    lines = file.readlines()
    fishies = [int(x) for x in lines[0].rstrip().split(",")]

# Variables
hatching = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for fish in fishies:
    hatching[fish] += 1

# Processing
for i in range(80):
    new_hatching = [hatching[1], hatching[2], hatching[3], hatching[4], hatching[5], hatching[6], hatching[7] + hatching[0], hatching[8], hatching[0]]
    hatching = new_hatching

# Output
print(f"How many lanternfish would there be after 80 days? {sum(hatching)}")

# -- Part 2 --

# Variables
hatching = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for fish in fishies:
    hatching[fish] += 1

# Processing
for i in range(256):
    new_hatching = [hatching[1], hatching[2], hatching[3], hatching[4], hatching[5], hatching[6], hatching[7] + hatching[0], hatching[8], hatching[0]]
    hatching = new_hatching

# Output
print(f"How many lanternfish would there be after 256 days? {sum(hatching)}")