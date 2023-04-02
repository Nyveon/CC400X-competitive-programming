# Eric K
# 31/03/2023
# CodeTON Round 4 - C

t = int(input())

for _ in range(t):
    n, c, d = [int(x) for x in input().split()]  # c: removal, d: insertion
    a = sorted([int(x) for x in input().split()])

    current_cost = (a[0] - 1) * d   # cost of filling up from 1
    min_cost = d + n * c            # cost of removing all and inserting 1
    skips = 0

    for i in range(n - 1):
        if skips > 0:
            skips -= 1
            continue

        min_cost = min((n - i - 1) * c + current_cost, min_cost)
        difference = a[i + 1] - a[i]
        if difference == 0:     # cost of removing this duplicate span
            end_index = i + 1
            while end_index < n - 1 and a[end_index + 1] == a[end_index]:
                end_index += 1
            current_cost += (end_index - i) * c
            skips = end_index - i - 1
        elif difference > 1:    # cost of filling up this gap
            current_cost += (difference - 1) * d

    min_cost = min(min_cost, current_cost)

    print(min_cost)
