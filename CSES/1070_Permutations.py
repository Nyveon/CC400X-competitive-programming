# Eric K
# 20/03/2023


# 1 2 3 4
# 1 4 2 3

n = int(input())

if n == 1:
    print(1)
    exit()

if n <= 3:
    print("NO SOLUTION")
    exit()

for digit in range(5, n + 1, 2):
    print(digit, end=" ")

print("2 4 1 3", end=" ")

for digit in range(6, n + 1, 2):
    print(digit, end=" ")
