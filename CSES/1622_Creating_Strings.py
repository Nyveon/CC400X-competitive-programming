# Eric K
# 20/03/2023

from itertools import permutations
words = sorted(list(set([''.join(x) for x in permutations(input())])))
print(f'{len(words)}\n' + '\n'.join(words))
