# Eric K
# 31/03/2023
# CodeTON Round 4 - B

t = int(input())

for _ in range(t):
    n = int(input())
    candy = 1

    if n % 2 == 0:
        print(-1)
        continue

    n = bin(n)[2:-1]
    if len(n) > 40:
        print(-1)
        continue

    print(len(n))
    for i in range(len(n)):
        if n[i] == "1":
            print(2, end=" ")
        else:
            print(1, end=" ")
    print()
