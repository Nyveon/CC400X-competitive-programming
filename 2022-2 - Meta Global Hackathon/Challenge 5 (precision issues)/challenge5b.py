# Eric K.
# Meta Global Hackathon 2022

from fractions import Fraction
from decimal import *
getcontext().prec = 128

# Input
lines = []
file_name = "ti.txt"
#file_name = "promotions_hard_input.txt"
with open(file_name, "r") as f:
    for line in f:
        lines.append(line.rstrip())


# Auxiliarry functions
lvl1 = Fraction(10**6)
lvl2 = Fraction(2*10**6)

def get_level(wage):
    if wage < lvl1:
        return 0
    elif wage < lvl2:
        return 1
    else:
        return 2

def to_decimal_string(frac):
    numerator = frac.numerator
    denominator = Decimal(frac.denominator)
    return str(Decimal(numerator/denominator).quantize(Decimal('0.000001')))

# Processing
ans_lines = []
t = int(lines[0])
lines = lines[1:]
for _ in range(t):
    n, q = [int(x) for x in lines[0].split()]
    wages = [Fraction(x) for x in lines[1].split()]
    lines = lines[2:]

    for _ in range(q):
        query = lines[0].split()
        print(wages)
        print(query)
        lines = lines[1:]
        if query[0] == "1": # Modify
            percentages = [Fraction(100 + int(x), 100) for x in query[1:4]]
            e, r = [int(x) for x in query[4:6]]
            e -= 1
            #levels = [get_level(wages[x]) for x in range(n)]
            for _ in range(r):
                for i in range(n):
                    wages[i] *= percentages[get_level(wages[i])]
                    #wages[i] *= percentages[levels[i]]
                print(to_decimal_string(wages[e]))
                print(wages[e])
                ans_lines.append(to_decimal_string(wages[e]))
        elif query[0] == "2": # Query
            e1, e2 = [int(x) - 1 for x in query[1:]]
            total = Fraction(0)
            for i in range(e1, e2+1):
                total += wages[i]
            print(to_decimal_string(total))
            ans_lines.append(to_decimal_string(total))
        print("========")
    print("x=x=x=x=x=x=x=x=x=x")

# Output
with open("out.txt", "w") as f:
    for line in ans_lines:
        f.write(line + "\n")