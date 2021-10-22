# [ Nyveon ]
# Tarea 2 Ejercicio 5
# E - Wi-Fi
# similar a las vacas ?
# pero como, opuesto

import sys
ITERATIONS = 50

def checker(houses, checking, access_points):

    used_points = 1
    position = houses[0] + checking     # current access point position
    for index in range(1, len(houses)):
        if abs(houses[index] - position) <= checking:
            continue

        position = houses[index] + checking     # current access point position
        used_points += 1                        # add to used points because a point has been placed

    return used_points <= access_points


test_cases = int(sys.stdin.readline())

for case in range(test_cases):

    # Input
    # n: Access points
    # m: Houses
    line = sys.stdin.readline()
    n, m = [int(x) for x in line.split()]

    houses = [] # List of house distances
    for i in range(m):
        line = sys.stdin.readline()
        houses.append(int(line))  # Times ten to divide later

    houses.sort()

    # Binary search on the answer
    #print(houses)
    left = 0
    right = houses[m - 1] + 1

    for b in range(ITERATIONS):
        mid = (right + left)/2

        if checker(houses, mid, n):
            right = mid
        else:
            left = mid

    sys.stdout.write(str(round(right, 2)) + "\n")