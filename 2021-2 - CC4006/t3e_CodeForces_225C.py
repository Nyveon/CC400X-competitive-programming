# [ Nyveon ]
# Tarea 3 Ejercicio 5
# E - Supermercado Lidor

# column -> (hashes (black), dots (white))
# because column(# . # # .) == column(# # # . .)
# (as far as operations it can handle goes)

import sys

# Input
line = sys.stdin.readline()
height, width, x, y = [int(x) for x in line.split()]
# n is height, m is width

black_columns = [0] * (width + 1)
white_columns = [0] * (width + 1)

# Storing input into columns
for row in range(1, height + 1):
    line = sys.stdin.readline().rstrip()
    index = 1
    for char in line:
        if char == "#":
            black_columns[index] += 1
        else:
            white_columns[index] += 1
        index += 1


# CUMSUM JAJAJAJAJ
cumsum_black = [0]
cumsum_white = [0]

for i in range(width):
    cumsum_black.append(cumsum_black[i] + black_columns[i + 1])
    cumsum_white.append(cumsum_white[i] + white_columns[i + 1])


# Processing
dp_black = [0]
dp_white = [0]

for i in range(1, width + 1):
    current_min_black_value = 2147483647
    current_min_white_value = 2147483647

    for j in range(x, y + 1):
        this_index = (i - j)

        if this_index < 0:
            break

        this_value_black = dp_white[this_index] + (cumsum_black[i] - cumsum_black[this_index])
        this_value_white = dp_black[this_index] + (cumsum_white[i] - cumsum_white[this_index])

        if this_value_black < current_min_black_value:
            current_min_black_value = this_value_black

        if this_value_white < current_min_white_value:
            current_min_white_value = this_value_white

    dp_black.append(current_min_black_value)
    dp_white.append(current_min_white_value)

answer = min(dp_black[width], dp_white[width])
sys.stdout.write(str(answer) + "\n")