# [ Nyveon ]
# Tarea 3 Ejercicio 4
# D - Combinación Piramidal

import sys

# Input
n = int(sys.stdin.readline())
line = sys.stdin.readline()
a = [int(x) for x in line.split()]
q = int(sys.stdin.readline())



# Processing the DP
dp_xor = [a]
dp_max = [a]
size = n

# XOR Pyramid
for i in range(n - 1):

    this_dp_xor = []
    this_dp_max = []

    for j in range(len(dp_xor[i]) - 1):
        this_value = dp_xor[i][j] ^ dp_xor[i][j + 1]
        this_dp_xor.append(this_value)
        this_dp_max.append(max((this_value, dp_max[i][j], dp_max[i][j + 1])))

    dp_xor.append(this_dp_xor)
    dp_max.append(this_dp_max)


# Queries
for i in range(q):
    line = sys.stdin.readline()
    l, r = [int(x) - 1 for x in line.split()]
    this_height = r - l

    if this_height < 1:
        sys.stdout.write(str(dp_xor[0][l]) + "\n")
    else:
        # All potential answers
        top = dp_xor[this_height][l]
        left = dp_max[this_height - 1][l]
        right = dp_max[this_height - 1][l + 1]

        answer = max((top, left, right))

        sys.stdout.write(str(answer) + "\n")