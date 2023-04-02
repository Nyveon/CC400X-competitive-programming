# Eric K.
# 23/03/2023
# Codeforces 1809 B

# Incomplete, WA

import math

# contest code
# off by one when nubmer are large  :(
# not enough precision?

# def inner_concentric(n):
#     return math.ceil((math.sqrt(n) - 1) / 2) * 2


# def outer_concentric(n):
#     return math.ceil(math.sqrt(n) / 2) * 2 - 1

# post-contest code

t = int(input())

for _ in range(t):
    n = int(input())  # up to 10^18

    cost = min(inner_concentric(n), outer_concentric(n))

    print(cost)
