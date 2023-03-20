# Eric K
# 20/03/2023

_ = int(input())
a = [int(x) for x in input().split()]
steps = 0

for index, number in enumerate(a):
    if index == 0:
        continue
    if a[index] < a[index-1]:
        steps += a[index-1] - a[index]
        a[index] = a[index-1]

print(steps)
