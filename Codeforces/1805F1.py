# Eric K
# 02/04/2023
# Codeforces Round 862 Problem F 1 (out of 2)
# TLe on test 12 :(

modulo = 10**9 + 7
biggest = 10**13  # might need to make this bigger

n = int(input())
a = sorted([int(x) for x in input().split()])


def weakest(a: list) -> list:
    n = len(a)
    result = []

    for i in range(n):
        for j in range(i + 1, n):
            result.append(a[i] + a[j])

    return sorted(result)[:n - 1]


while (len(a) > 1):
    a = weakest(a)

print(a[0] % modulo)
