# Eric
# Tarea 5 Ejercicio 2
# B - Pasión por los Palíndromos

import sys

# Input
s = sys.stdin.readline().rstrip()
ls = len(s)

# Variables
power = 127
power_backwards = 1
mod = 1000000007
hash_forwards = 0
hash_backwards = 0
degrees = [0]*ls
count = 0

# Processing
for i in range(ls): #5*10^6
    hash_forwards = (ord(s[i]) + hash_forwards * power) % mod
    hash_backwards = (ord(s[i]) * power_backwards + hash_backwards) % mod
    power_backwards = (power_backwards*power) % mod
    print(hash_forwards, hash_backwards)

    if hash_backwards == hash_forwards:
        degrees[i] = degrees[(i-1)//2] + 1
        count += degrees[i]

# Output
sys.stdout.write(str(count) + "\n")