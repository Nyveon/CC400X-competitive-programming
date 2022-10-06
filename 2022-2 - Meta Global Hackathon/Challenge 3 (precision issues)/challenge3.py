# Eric K.
# Meta Global Hackathon 2022

from math import comb
from fractions import Fraction

# Input
lines = []
file_name = "test_input.txt"
file_name = "wanikani_hard_input.txt"
with open(file_name, "r") as f:
    for line in f:
        lines.append(line.rstrip())

# Input Processing
T = int(lines[0])
lines = lines[1:]


def sep():
    print("=======================")


def format(x):
    # Round to 6 digits
    # x = x.denominator / x.numerator
    x = float(x)
    x = round(x, 6)
    # Convert to string padding with 0s
    return '{:.6f}'.format(x)


expecteds = []
for query in range(T):
    # N: Number of kanji in the deck
    # K: Reviewed kanji
    N, K = [int(x) for x in lines[query].split()]

    print(f"Query {query+1}: N={N}, K={K}")

    # Iterate through potential values of asked cards
    least_asked = K * 2
    most_a = K * 2 + (N - K)
    most_n = 2 * N
    most_asked = min(most_a, most_n)
    print(f"Least asked: {least_asked},\
           most asked: {most_asked} ({most_a} {most_n})")

    probabilities = []
    for M in range(least_asked, most_asked + 1):
        P = Fraction((comb(N - K, M - 2 * K) * comb(N, K)
                     * (2 ** (M - 2*K))), ((2 * N + 1) * comb(2*N, M)))
        probabilities.append(P)

    # Sum probabilities
    Ptotal = Fraction(0)
    for P in probabilities:
        Ptotal += P

    expected = Fraction(0)
    for M in range(least_asked, most_asked + 1):
        R = Fraction(N*2 - M)
        X = probabilities[M - least_asked] / Ptotal
        # print(f"M={M}, X={X}, RX={M*X}")
        expected += R * X
    expecteds.append(format(expected))
    print(f"Expected: {format(expected)}")
    sep()

# Output
with open("out.txt", "w") as f:
    for answer in expecteds:
        f.write(answer + '\n')
