# Nyveon
# Advent of code 2020
# Day 7
# Python 3


# -- Input --
file = open("day7_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()
file.close()
rules = file_in.split("\n")
rules.pop()

# Parsing input
bags = {}
for i in rules:
    a = i.split()
    bag_id = a[0] + a[1]
    a = a[4:]
    rule = []
    if a[0] == "no":
        rule.append((0, 0))
    else:
        while(len(a) > 2):
            rule.append((a[1] + a[2], a[0]))
            a = a[4:]
    bags[bag_id] = rule

print(bags)

# Searching
target = "shinygold"

def bag_search(key):
    ans = False
    for item in bags[key]:
        if item[0] == target:
            ans = True
        elif item[0] == 0:
            ans = ans or False
        else:
            ans = ans or bag_search(item[0])
    return ans

count = 0
for key in bags:
    if bag_search(key):
        count += 1
print("Part 1:", count)



# -- Part 2 --

def bag_count(key, m):
    count = 0
    for item in bags[key]:
        if item[0 != 0]:
            count += int(item[1]) * m
            count += m*bag_count(item[0], int(item[1]))
    return count

print("Part 2:", bag_count("shinygold", 1))
