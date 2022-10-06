# Eric K.
# Meta Global Hackathon 2022

import multiprocessing
import time

# Input
lines = []
file_name = "zigzag_hard_input.txt"
# file_name = "test_input.txt"
with open(file_name, "r") as f:
    for line in f:
        lines.append(line)

N = int(lines[0])
line_pointer = 1


# Generated an empty grid
def empty_grid():
    grid = []
    for i in range(9):
        grid.append([])
        for j in range(9):
            grid[i].append(0)
    return grid


# Make input grids
grids = []
for case in range(N):
    # Read in the grid
    grid = empty_grid()
    for row in range(9):
        this_line = lines[line_pointer].rstrip().split(' ')
        for col in range(9):
            cell = this_line[col]
            if cell != '.':
                grid[row][col] = int(cell)
            else:
                grid[row][col] = -1
        line_pointer += 1
    grids.append(grid)
    line_pointer += 1

# Processing


# Checks if a given grid is valid
def is_valid(grid, row, col, num):
    # Check diagonally to the right, with offset modulo
    for i in range(9):
        if grid[(row + i) % 9][(col + i) % 9] == num:
            return False

    # Check diagonal zags
    for i in range(9):
        if grid[(row + i) % 9][(col - i) % 9] == num:
            return False

    # Check square
    for i in range(3):
        for j in range(3):
            if grid[(row // 3) * 3 + i][(col // 3) * 3 + j] == num:
                return False

    return True


# Solves a grid with backtracking
def solve(grid):
    # Find an empty cell
    for row in range(9):
        for col in range(9):
            if grid[row][col] == -1:
                # Try all numbers
                for num in range(9):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid)[0]:
                            return (True, grid)
                        grid[row][col] = -1
                return (False, grid)
    return (True, grid)


if __name__ == '__main__':
    start = time.time()
    pool = multiprocessing.Pool(8)
    results = pool.map(solve, grids)
    end = time.time()
    print(end - start)

    value = 0
    for result in results:
        print(result[1][0][0], value)
        value += result[1][0][0]

    with open("debugout.txt", "w") as f:
        f.write(str(result))

    with open("out.txt", "w") as f:
        f.write(str(value))
