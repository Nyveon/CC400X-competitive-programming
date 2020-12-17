# Nyveon
# Advent of code 2020
# Day 16
# Python 3

# -- Input --
file = open("day16_input.txt", "r")
#file = open("test.txt", "r")
file_in = file.read()[:-1]
file.close()
lines = file_in.split("\n\n")
import random


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
print("Part 1:", scanning_error)


# -- Part 2 --
# Finish later
# Input parsing

# Remove invalid tickets
tickets_new = []
for i in range(len(tickets)):
    if i not in invalid_indexes:
        tickets_new.append(tickets[i])
tickets = tickets_new

# Make dictionary of rules
rules_keys = lines[0].split("\n")
rules_dict = {}
for i in range(len(rules_keys)):
    rules_dict[rules_keys[i].split(":")[0]] = rules[i]
field_map = []
for i in range(fields):
    field_map.append([])

# Find corresponding rules
for field in range(fields): # For each field
    for key in rules_dict: # For each rule
        corresponds = True
        for ticket in range(len(tickets)): # For each ticket
            if not ((rules_dict[key][0] <= tickets[ticket][field] <= rules_dict[key][1]) or (rules_dict[key][2] <= tickets[ticket][field] <= rules_dict[key][3])):
                corresponds = False
                break
        if corresponds:
            field_map[field].append(key)

# Find the right combination of potential fields so that each one is unique
field_map_final = []
for i in range(fields):
    field_map_final.append(0)

removed_count = 0
while removed_count < fields:
    for i in range(len(field_map)):
        if len(field_map[i]) == 1:
            remover = field_map[i][0]
            for j in range(len(field_map)):
                if remover in field_map[j]:
                    field_map[j].remove(remover)
            field_map_final[i] = remover
            field_map[i] = [0, 0]
            removed_count += 1
            break

answer = 1
for i in range(len(field_map_final)):
    if "departure" in field_map_final[i]:
        answer = answer * my_ticket[i]
print("Part 2:", answer)
