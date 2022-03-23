# Nyveon
# T0 CC4005
# Problem C - Emilia y el cerco

# Input
line = input()
n, h = [int(x) for x in line.split()]
line = input()
a = [int(x) for x in line.split()]

# Processing
total = 0
for height in a:
    if height > h:
        total += 2
    else:
        total += 1

# Output
print(total)
