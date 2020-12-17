# Nyveon
# Advent of code 2020
# Day 16
# Python 3

# -- Input --
#file = open("day16_input.txt", "r")
file = open("test.txt", "r")
file_in = file.read()[:-1]
file.close()
lines = file_in.split("\n\n")


# -- Part 1 --

# Input parsing
rules = lines[0].split("\n")
for i in range(len(rules)):
    rules[i] = rules[i].split(": ")[1]
    temp1 = rules[i].split("-")
    temp2 = temp1[1].split(" or ")
    rules[i] = [int(temp1[0]), int(temp2[0]), int(temp2[1]), int(temp1[2])]

my_ticket = lines[1][13:].split(",")

for i in range(len(my_ticket)):
    my_ticket[i] = int(my_ticket[i])


tickets = lines[2][16:].split("\n")

for i in range(len(tickets)):
    tickets[i] = tickets[i].split(",")
    for j in range(len(tickets[i])):
        tickets[i][j] = int(tickets[i][j])

fields = len(tickets[0])
print(rules)

# Main solver
invalid_values = []
invalid_indexes = []
for i in range(len(tickets)):
    valid_counter = 0
    for j in range(len(tickets[i])):
        valid = False
        for k in range(len(rules)):
            if (rules[k][0] <= tickets[i][j] <= rules[k][1]) or (rules[k][2] <= tickets[i][j] <= rules[k][3]):
                valid = True
                break
        if not valid:
            invalid_values.append(tickets[i][j])
            invalid_indexes.append(i) # For part 2

scanning_error = 0
for i in invalid_values:
    scanning_error += i
print(invalid_values)
print(invalid_indexes)
print("Part 1:", scanning_error)


# -- Part 2 --
# Finish later
# Input parsing
rules_keys = lines[0].split("\n")
rules_dict = {}
for i in range(len(rules_keys)):
    rules_dict[rules_keys[i].split(":")[0]] = rules[i]

for i in range(fields):
    print("Field:", i)
    for j in range(len(tickets)):
        print("Value:", tickets[j][i])
        for key in rules_dict:
            print(key)
            found_key = key
            rule_found = True
            print(rules_dict[key])
            if (rules_dict[key][0] <= tickets[j][i] <= rules_dict[key][1]) or (rules_dict[key][2] <= tickets[j][i] <= rules_dict[key][3]):
                print("stinky")
                rule_found = False
                break
        if rule_found:
            print("Rule found, key:", found_key)

    print("----")


