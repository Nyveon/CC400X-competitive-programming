# Eric K
# 30/03/2023

# pending

n = int(input())

numbers = []
target = 2**n

for i in range(target):
    numbers.append(bin(i)[2:].zfill(n))

print(numbers[::2])
