# Eric K.
# Meta Global Hackathon 2022
from fractions import Fraction

def get_level(x):
    if x < 10**6:
        return 0
    elif x < 2*10**6:
        return 1
    else:
        return 2

def output_format(x):
    #val = x.__round__(6) # Future eric: maybe not round
    return '{:.7f}'.format(float(x))

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
    # Number of employees and number of queries
    n, q = map(int, lines[0].split())

    # Starting wages
    wages = list(map(Fraction, lines[1].split()))
    multipliers = [Fraction(1) for _ in range(n)]

    # Queries
    for i in range(q):
        query = [int(x) for x in lines[i + 2].split()]
        print(query)
        if query[0] == 1: # Update tree
            percentages = [query[1], query[2], query[3]]
            percentages = [Fraction(x, 100) for x in percentages]
            e = query[4] - 1 # Employee ID
            r = query[5] # Number of times the query happens
            for _ in range(r):
                for j in range(n):
                    level = get_level(wages[j] * multipliers[j])
                    multipliers[j] *=  Fraction(1) + percentages[level]
                    multipliers[j] = multipliers[j].limit_denominator(100000000000)
                ans = wages[e] * multipliers[e]
                ans_lines.append(output_format(ans))
                print(output_format(ans))
        elif query[0] == 2: # Query tree
            e1 = int(query[1]) - 1
            e2 = int(query[2]) - 1
            ans = Fraction(0)
            for j in range(e1, e2+1):
                ans += wages[j] * multipliers[j]
            print(output_format(ans))
            ans_lines.append(output_format(ans))
        print("==============")

    # Remove first part of lines
    lines = lines[2 + q:]


# Output
with open("out.txt", "w") as f:
    for ans in ans_lines:
        f.write(ans + "\n")