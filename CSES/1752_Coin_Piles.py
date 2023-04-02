# Eric K
# 30/03/2023

# pending

t = int(input())

for _ in range(t):
    a, b = [int(x) for x in input().split()]
    if a % 2 == 0 and b % 2 == 0:
        print("NO")
    else:
        print("YES")
