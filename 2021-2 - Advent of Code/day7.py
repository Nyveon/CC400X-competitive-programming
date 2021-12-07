"""
Eric AKA Nyveon
https://adventofcode.com/2021/day/7
"""

# -- Part 1 --

# Input
with open("day7.txt", 'r') as file:
    lines = file.readlines()
    crabs = [int(x) for x in lines[0].rstrip().split(",")]

# Variables
min_crab = min(crabs)
max_crab = max(crabs)
min_fuel = int(1e12)

# Processing
for i in range(min_crab, max_crab+1):

    fuel = 0
    for crab in crabs:
        fuel += abs(crab - i)

    if fuel < min_fuel:
        min_fuel = fuel


# Output
print(f"P1: How much fuel must they spend to align to that position? {min_fuel}")


# -- Part 2 --

# Variables
min_fuel = int(1e12)

# Processing
for i in range(min_crab, max_crab+1):

    fuel = 0
    for crab in crabs:
        distance = abs(crab - i)
        fuel += (distance+1)*distance//2

    if fuel < min_fuel:
        min_fuel = fuel

# Output
print(f"P2: How much fuel must they spend to align to that position? {min_fuel}")
