# Eric
# Tarea 5 Ejercicio 1
# A - Tarea Trivialn


import sys

# Input
T = int(sys.stdin.readline())

# Process
for i in range(T):
    s, p = sys.stdin.readline().rstrip().split(" ")
    x = s.find(p)
    if x == -1:
        sys.stdout.write("Not Found\n")
        continue

    indexes = [x + 1]
    while True:
        x = s.find(p, x+1)
        if x == -1:
            break
        indexes.append(x + 1)

    sys.stdout.write(str(len(indexes)) + "\n")
    sys.stdout.write(str(" ".join(map(str, indexes))) + "\n")

