"""
Eric AKA Nyveon
https://adventofcode.com/2021/day/1
"""

# -- Part 1 --

# Input
with open("day1.txt", 'r') as file:
    depths = file.readlines()
    depths = [int(line) for line in depths]
    depths_copy = depths.copy()

# Processing
previous_depth = depths.pop(0)
depth_increases = 0
for depth in depths:
    if depth > previous_depth:
        depth_increases += 1
    previous_depth = depth

# Output
print(f"How many measurements are larger than the previous measurement? {depth_increases}")

# -- Part 2 --

# Processing
depths = depths_copy
rolling_sum = depths[0] + depths[1] + depths[2]
rolling_sum_increases = 0
for index in range(3, len(depths)):
    previous_rolling_sum = rolling_sum
    rolling_sum += depths[index]
    rolling_sum -= depths[index-3]
    if rolling_sum > previous_rolling_sum:
        rolling_sum_increases += 1

# Output
print(f"How many sums are larger than the previous sum? {rolling_sum_increases}")
