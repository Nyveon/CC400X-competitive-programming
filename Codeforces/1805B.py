# Eric K
# 02/04/2023
# Codeforces Round 862 Problem B

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    first = s[0]
    smallest = first
    smallest_index = -1

    for i in range(1, n):
        if s[i] <= smallest:
            smallest = s[i]
            smallest_index = i

    if smallest_index == -1:
        print(s)
    else:
        new = smallest + s[:smallest_index] + s[smallest_index+1:]
        if new <= s:
            print(new)
