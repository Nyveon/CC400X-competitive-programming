# Eric K
# 20/03/2023

n = int(input())

while n != 1:
    print(n, end=" ")
    if n % 2 == 0:
        n = n >> 1
    else:
        n = n * 3 + 1
print(n)
