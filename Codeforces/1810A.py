# Eric K
# 31/03/2023
# CodeTON Round 4 - A

t = int(input())


for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    for i in range(n):
        if a[i] <= i + 1:
            print("YES")
            break
    else:
        print("NO")
