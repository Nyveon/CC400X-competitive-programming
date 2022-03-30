# Nyveon (Eric K)
# T1 CC4005
# Problem B - Entrenamiento

# Input
n = int(input())
a = sorted([int(x) for x in input().split()])

# Processing
current = 1
participated = 0

for i in a:
    if current <= i:
        current += 1
        participated += 1

# Output
print(participated)
