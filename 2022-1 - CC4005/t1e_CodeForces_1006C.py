# Nyveon (Eric K)
# T1 CC4005
# Problem E - Subsegmentos Consecutivos

import math

# Input
n = int(input())
d = [int(x) for x in input().split()]
middle = math.ceil(n/2)

# Processing

# Potential s1s
previous = d[0]
potential_s1s = {previous: 0}
for i in range(1, n):
    current = d[i] + previous
    previous = current
    potential_s1s[current] = i

# Potential s3s
max_s1 = 0
potential_s3 = 0
checking_index = 0

for i in range(n-1, -1, -1):
    potential_s3 += d[i]

    if potential_s3 in potential_s1s:
        if i > potential_s1s[potential_s3]:
            max_s1 = potential_s3

# Output
print(max_s1)
