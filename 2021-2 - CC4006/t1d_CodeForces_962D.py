# [Nyveon]
# Tarea 1 Ejercicio 4
# D - Merge Equals
# finalmente, un ejercicio resolvible ne python??

import sys

# Input
n = int(sys.stdin.readline())
array = [int(x) for x in sys.stdin.readline().split()]
array_dict = {}

# this might depend on dictionaries staing sorted??
for i in range(len(array)):
    number = array[i]
    while number in array_dict:
        del array_dict[number]
        number *= 2
    array_dict[number] = i

# Output
ans_string = ""
ans_number = 0
for key in array_dict:
    ans_string += str(key) + " "
    ans_number += 1
print(ans_number)
print(ans_string[:-1])