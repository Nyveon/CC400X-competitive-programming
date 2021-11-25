# Eric
# Tarea 5 Ejercicio 4
# D - Lista de Limpieza

import sys, itertools

def modified_rabin_karp(text, pattern_length, hash_set):
    p1 = 227
    m1 = int(1e9) + 9

    p2 = 31
    m2 = int(1e9) + 7

    text_length = len(text)

    power1 = 1
    power2 = 1
    for i in range(pattern_length - 1):
        power1 = (power1 * p1) % m1
        power2 = (power2 * p2) % m2


    hs1 = 0
    hs2 = 0
    for i in range(pattern_length):
        hs1 = (hs1 * p1 + (ord(text[i]) - ord('a'))) % m1
        hs2 = (hs2 * p2 + (ord(text[i]) - ord('a'))) % m2
    hsc = int(str(hs1) + str(hs2))
    hash_set.add(hsc)

    for i in range(pattern_length, text_length):
        hs1 = ((hs1 - power1 * (ord(text[i - pattern_length]) - ord('a')) + 2 * m1) * p1 + (ord(text[i]) - ord('a'))) % m1
        hs2 = ((hs2 - power2 * (ord(text[i - pattern_length]) - ord('a')) + 2 * m2) * p2 + (ord(text[i]) - ord('a'))) % m2
        hsc = int(str(hs1) + str(hs2))
        hash_set.add(hsc)


T = int(sys.stdin.readline())

for x in range(T):
    n, k = map(int, sys.stdin.readline().split(" "))
    s = sys.stdin.readline().rstrip()
    instructions = set()
    modified_rabin_karp(s, k, instructions)
    sys.stdout.write(str(len(instructions)) + "\n")