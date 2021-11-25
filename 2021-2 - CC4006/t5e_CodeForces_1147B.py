# Eric
# Tarea 5 Ejercicio 5
# E - Sapo, Sepo y Simetrias

import sys, collections, bisect

# Input
n, m = (int(x) for x in sys.stdin.readline().split())
adjacency = collections.defaultdict(lambda: [])
for i in range(m):
    a, b = (int(x) for x in sys.stdin.readline().split())
    bisect.insort(adjacency[a], (b - a) % n)
    bisect.insort(adjacency[b], (a - b) % n)

# String conversion
string = '|'.join(','.join(str(i) for i in adjacency[i]) for i in range(n+1))

# Search
searchstring = string*2
if string not in searchstring[1:-1]:
    print("No")
else:
    print("Yes")