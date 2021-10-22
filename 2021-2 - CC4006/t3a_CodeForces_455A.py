# [ Nyveon ]
# Tarea 3 Ejercicio 1
# A - Jorge y Secuencias


import sys
from collections import defaultdict

# Input
n = int(sys.stdin.readline())
line = sys.stdin.readline()
array = [int(x) for x in line.split()]
frequency = defaultdict(int)

max_number = -1
for number in array:
    if number > max_number:
        max_number = number
    frequency[number] += 1


# Solution
scores = [0]

for index in range(max_number + 1):

    this_number = frequency[index + 1] * (index + 1)
    p_number = scores[index]
    pp_number = scores[index - 1]

    scores.append(max(pp_number + this_number, p_number))

# Output
print(scores[max_number])