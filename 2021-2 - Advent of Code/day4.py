"""
Eric AKA Nyveon
https://adventofcode.com/2021/day/4
"""

# Imports
from collections import defaultdict

# -- Part 1 --

# Input
with open("day4.txt", 'r') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

order = [int(x) for x in lines.pop(0).split(",")]

# Pre-processing
boards = []
board_number = -1
row_number = 0
for line in lines:
    if line == '':
        board_number += 1
        row_number = 0
        boards.append(defaultdict(lambda: (-1, -1)))
    else:
        row = [int(x) for x in line.split()]
        for index, item in enumerate(row):
            boards[board_number][item] = (row_number, index)
        row_number += 1

# Variables
board_results = []
for i in range(len(boards)):
    board_results.append([defaultdict(int), defaultdict(int), 0]) # Rows, Columns, Called
win = False

# Processing
for number in order:
    for index, board in enumerate(boards):
        if board[number][0] != -1:
            board_results[index][2] += number
            board_results[index][0][board[number][0]] += 1
            if board_results[index][0][board[number][0]] == 5:
                win = True
                winner = index
            board_results[index][1][board[number][1]] += 1
            if board_results[index][1][board[number][1]] == 5:
                win = True
                winner = index

    if win:
        break

sum = -board_results[winner][2]
for key in boards[winner]:
    if boards[winner][key][0] != -1:
        sum += key
score = sum * number

# Output
print(f"What will your final score be if you choose that board? {score}")


# -- Part 2 --

# Variables
board_results = []
for i in range(len(boards)):
    board_results.append([defaultdict(int), defaultdict(int), 0]) # Rows, Columns, Called
winners = []

# Processing
for number in order:
    for index, board in enumerate(boards):
        if index not in winners:
            if board[number][0] != -1:
                board_results[index][2] += number
                board_results[index][0][board[number][0]] += 1
                if board_results[index][0][board[number][0]] == 5:
                    winners.append(index)
                    final_number = number
                board_results[index][1][board[number][1]] += 1
                if board_results[index][1][board[number][1]] == 5:
                    winners.append(index)
                    final_number = number

    if len(winners) == len(boards):
        break

winner = winners[-1]
sum = -board_results[winner][2]
for key in boards[winner]:
    if boards[winner][key][0] != -1:
        sum += key
score = sum * final_number

print(f"Once it wins, what would its final score be? {score}")
