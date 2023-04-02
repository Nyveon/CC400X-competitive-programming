# Eric K.
# 23/03/2023
# Codeforces 1809 A

from collections import Counter

t = int(input())


for _ in range(t):
    x = sorted(Counter(input()).values())

    # 4 types
    if x == [1, 1, 1, 1]:  # abcd
        print(4)
        continue

    # 3 types
    if x == [1, 1, 2]:  # aabc
        print(4)
        continue

    # 2 types
    if x == [2, 2]:  # aabb
        print(4)
        continue

    if x == [1, 3]:  # abbb
        print(6)
        continue

    # 1 types
    if x == [4]:  # aaaa
        print(-1)
        continue
