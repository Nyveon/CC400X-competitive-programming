# [ Nyveon ]
# Tarea 2 Ejercicio 3
# C - Sapo y Sepo

import sys

# Input
line = sys.stdin.readline()
rocks, max_jump = [int(x) for x in line.split()]
line = sys.stdin.readline()
heights = [int(x) for x in line.split()]


# Solution
dp = [0]
for i in range(1, rocks):
    current_min_value = 2147483647
    for j in range(max_jump):
        if i - j < 1: # Don't check non-existent values
            continue

        this_index = (i - j - 1)
        this_cost = abs(heights[i] - heights[this_index]) + dp[this_index]
        if this_cost < current_min_value:
            current_min_value = this_cost

    dp.append(current_min_value)

# Output
sys.stdout.write(str(dp[rocks - 1]) + "\n")
