# Nyveon (Eric K)
# T1 CC4005
# Problem A - MCFC en la salita

# Input
# n: number of players
# k: number of victories needed
# a: level of the ith player
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

# Processing & Output
current_streak = 0
current = a[0]

for i in range(1, n):
    value = a[i]

    # Streak win or THE BEST edge case
    if current_streak >= k or current == n:
        print(current)
        break

    # THE BEST
    if value == n:
        print(value)
        break

    # Streak upset
    if value > current:
        current = value
        current_streak = 1
    else:
        current_streak += 1
