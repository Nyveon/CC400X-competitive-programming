# Eric K.
# 22/03/2023

n = int(input())

modulo = 10**9 + 7
x = 2

if n == 0:
    print(1)
    exit()

if n == 1:
    print(2)
    exit()

for i in range(1, n):
    x = (x % modulo * 2) % modulo

print(x)
