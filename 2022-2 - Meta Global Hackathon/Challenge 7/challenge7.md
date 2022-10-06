# Micro Kitchens

## Problem

You are a space planner for a new start-up and need to find the ideal spots in the office to put micro kitchens.

You must make it as easy as possible to get to by finding all the spots that minimize the sum of distances from that spot to all employees in the office. The distance to an employee is the number of moves on the shortest path moving left, right, up, or down (but not diagonally) by one cell at a time. There are E employees in the office.

Your startup has outgrown its office yet again and is planning another move. Luckily, the new office doesn't introduce any more exotic architecture (like walls), but it will be spread out over multiple floors, connected by flights of stairs. Each floor features exactly one flight of stairs.

The constraints for movement and placing of the micro kitchen remain the same as in the single-floor layout:

- Walls still obstruct employees' movements
- Employees cannot walk through each others' desk areas.
- Employees cannot share the same space with a micro kitchen.

The office employs a modern design that doesn't require flights of stairs to be in the same position in every floor. Moving up or down a floor doesn't take any effort for employees either, meaning the cost of moving between floors is 0 and an employee standing on a flight of stairs is one move away from the spots adjacent to stairs on all floors.

What are all the F, X, and Y coordinates of the best spots to put micro kitchens, given that (0,0,0) is in the top-left corner of the 0th floor, with F coordinates increasing for successive floors, X coordinates increasing from left to right, and Y coordinates increasing from top to bottom? It's not guaranteed that a unique best spot, your job is to find all of them and show them in increasing order by F, then by X and then by Y

## Input

Your input specifies the layout of the office as follows:

- The first line contains 3 numbers: W, H, and N, representing the width, height and number of floors in the office.
- What follows is N sets of lines, with the ith set describing the ith floor:
  - Each set consists of H lines that are W characters wide.
  - Sets are separated by an empty line.
  - The (j,k)-th cell in the set (j characters from the left and k characters from the top of the set) represents the contents at position (j,k) of the ith floor. Each cell will be one of the following:
    - "." - An empty space
    - "o" - An employee's desk area
    - "w" - A wall
    - "s" - A flight of stairs (occurring exactly once per floor)

## Output

Your output should be a file containing a single line with all the tuples with the (F,X,Y) coordinates of the optimal spots to put the micro kitchen in separated by a space, sorted lexicographically

## Constraints

- 0 ≤ F < N
- 0 ≤ X < W
- 0 ≤ Y < H
- 1 ≤ W ≤ 50
- 1 ≤ H ≤ 50
- 1 ≤ N ≤ 10
- 1 ≤ E ≤ 50

## Explanation of Sample

There are 10 employees in the office across 3 floors, which makes it so that four spots minimize the sum of the distances that employees have to walk to get to the micro kitchen is; those spots are (0, 3, 5), (1, 3, 6), (1, 4, 5) and (2, 3, 2)

Sample Input

```text
. . . . . . . . . .
. w o . . . . . . .
. . w . . . . w . .
. . . w o . . . . .
w . . s w . . . . .
. . . . . . . . . .
. . . . . . . . . .
. . w . . . . . . .
. . . . . . . . . w
. . . . . . . o w .

. . o . . w w . . .
. . . . o . . . . .
. . . . w . . w . w
. . . . o . w . . .
. . . . w w . . . .
w . . . . . . . . .
. . . . s . . . . .
. w w . . w . . . .
w . . . . . . . o .
. . . . . w w . w w

. w . . . . . . w .
. . w s . . . . w .
. . . . . . . . . .
. . . . w . w . . .
o . . . o . . . . o
. w . . . . . . . w
w w . w w . . . . .
. w . w . . . . . .
. . . . . . . w . w
. w w . . w . . . .
```

Sample Output

```text
(0, 3, 5) (1, 3, 6) (1, 4, 5) (2, 3, 2)
```
