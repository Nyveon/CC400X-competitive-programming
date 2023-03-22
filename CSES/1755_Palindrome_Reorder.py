# Eric K
# 20/03/2023

from collections import Counter

letters = Counter(input())

# Discard impossibilities and find middle
odd = None
for key, value in letters.items():
    if value % 2 != 0:
        if odd is not None:
            print("NO SOLUTION")
            exit()
        odd = key

# Build palindrome
first = ""
middle = odd * letters[odd] if odd is not None else ""
second = ""

for key, value in letters.items():
    if key != odd:
        first += key * (value // 2)

second = first[::-1]

print(first + middle + second)
