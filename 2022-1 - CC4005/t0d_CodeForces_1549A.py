# Nyveon
# T0 CC4005
# Problem D - Eduardo y criptografía

# Input
t = int(input())
primes = []
for i in range(t):
    primes.append(int(input()))


# Processing & Output
for P in primes:
    print(2, P - 1)
