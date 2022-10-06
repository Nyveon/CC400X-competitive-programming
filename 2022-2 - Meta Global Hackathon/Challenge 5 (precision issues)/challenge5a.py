# Eric K.
# Meta Global Hackathon 2022

from fractions import Fraction
from decimal import *

def get_level(x):
    if x < 10**6:
        return 0
    elif x < 2*10**6:
        return 1
    else:
        return 2

def output_format(x):
    #val = x.__round__(6) # Future eric: maybe not round
    return '{:.6f}'.format(round(x, 6))
    #return '{:.6f}'.format(x)

def Kahan_Sum(x):
    ksum = 0
    c = 0
    for i in x:
        y = i - c
        t = ksum + y
        c = (t - ksum) - y
        ksum = t
    return ksum

# Input
lines = []
file_name = "test_input.txt"
#file_name = "promotions_hard_input.txt"
with open(file_name, "r") as f:
    for line in f:
        lines.append(line.rstrip())

# Processing
test_cases = int(lines[0])
lines = lines[1:]
ans_lines = []

for t in range(test_cases):
    n, q = [int(x) for x in lines[0].split()] # Number of employees and number of queries
    wages = [int(x) for x in lines[1].split()] # Starting wages
    print(t)

    for i in range(q): # Queries
        query = [int(x) for x in lines[i + 2].split()]
        print(f"{i}/{q}")
        print(query)
        if query[0] == 1:
            percentages = [query[1], query[2], query[3]]
            percentages = [100 + x for x in percentages]
            e = query[4] - 1 # Employee ID
            r = query[5] # Number of times the query happens
            for _ in range(r):
                for j in range(n):
                    level = get_level(wages[j])
                    wages[j] *= (percentages[level])/100
                    #wages[j] /= 100
                ans = wages[e]
                ans_lines.append(output_format(ans))
                print(output_format(ans))
        elif query[0] == 2: # Query tree
            e1 = int(query[1]) - 1
            e2 = int(query[2]) - 1
            # Get sum of wages from e1 to e2
            ans = Kahan_Sum(wages[e1:e2+1])
            print(output_format(ans))
            ans_lines.append(output_format(ans))
        print("==============")

    # Remove first part of lines
    lines = lines[2 + q:]
    print("x=x=x=x=x=x=x=x=x=x=x=x=x=x=x")


# Output
with open("out.txt", "w") as f:
    for ans in ans_lines:
        f.write(ans + "\n")