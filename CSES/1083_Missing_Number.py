# Eric K
# 20/03/2023

n = int(input())
a = [int(x) for x in input().split()]

# Sort then find worst case:
# n*log(n) + n
# Iterate through list and find worst case:
# 2*n (better, but how to implement?)

a.sort()
a.append(0)
counter = 1
for value in a:
    if counter != value:
        print(counter)
        break
    counter += 1
