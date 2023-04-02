# Eric K
# 02/04/2023
# Codeforces Round 862 Problem A

t = int(input())

highest = 2**8

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    answer = -1

    for i in range(highest):  # 256 * 10^3
        result = 0
        for j in range(n):
            result ^= a[j] ^ i
        if result == 0:
            answer = i
            break

    print(answer)
