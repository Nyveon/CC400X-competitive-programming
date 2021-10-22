"""
[ Nyveon ]
D - Sapo y Sepo practican alpinismo
"""

import sys

# Input
line = sys.stdin.readline()
miradores, max_jump = [int(x) for x in line.split()]
line = sys.stdin.readline()
heights = [int(x) for x in line.split()]

heights_delta = []
for i in range(miradores - 1):
    heights_delta.append(heights[i + 1] - heights[i])
heights_delta.reverse()

runs_dp = [0]
max_run = -1
i = 0
for delta in heights_delta:

    if delta <= max_jump:
        this_dp = runs_dp[i] + 1
    else:
        this_dp = 0

    runs_dp.append(this_dp)

    if this_dp > max_run:
        max_run = this_dp

    i += 1
sys.stdout.write(str(max(1, max_run + 1)) + "\n")
