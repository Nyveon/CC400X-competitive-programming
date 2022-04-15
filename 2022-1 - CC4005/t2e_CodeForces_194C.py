# Nyveon (Eric K)
# T2 CC4005
# Problem E - Sapo y Sepo odian a todos

# Data structure
from collections import deque
directions_x = (1, 0, -1, 0)
directions_y = (0, 1, 0, -1)


def output(number):
    print(number)
    quit()


def valid_road(graph, visited, x, y, width, height):
    if x < 0 or y < 0 or x >= width or y >= height:
        return False
    elif graph[y][x] != 1:
        return False
    elif visited[y][x]:
        return False
    else:
        return True


def bfs(graph, start_x, start_y, width, height, visited):
    """
    Breadth first search
    """
    visited[start_y][start_x] = True

    queue = deque([(start_x, start_y)])
    popped = 0

    while queue:
        s = queue.popleft()

        popped += 1
        x = s[0]
        y = s[1]

        for direction in range(4):
            adjacent_x = x + directions_x[direction]
            adjacent_y = y + directions_y[direction]
            if valid_road(graph, visited, adjacent_x, adjacent_y, width, height):
                queue.append((adjacent_x, adjacent_y))
                visited[adjacent_y][adjacent_x] = True

    return popped


# Input
n, t = [int(x) for x in input().split()]

grid = [[-1 for y in range(t)] for x in range(n)]
counter = 0
alpha_road = -1
beta_road = -1

for y in range(n):
    line = input().rstrip()
    for x, character in enumerate(line):
        number = 0
        if character == "#":
            beta_road = alpha_road
            alpha_road = (x, y)
            counter += 1
            number = 1
        grid[y][x] = number

# Processing

# Edge case: 2 or fewer tiles
if counter <= 2:
    output(-1)

# Single disconnection case:
for y in range(n):
    for x in range(t):
        if grid[y][x] == 1:

            result = True
            visited = [[False for y in range(t)] for x in range(n)]
            visited[y][x] = True
            if (x, y) == alpha_road:
                result = bfs(grid, beta_road[0], beta_road[1], t, n, visited)
            else:
                result = bfs(grid, alpha_road[0], alpha_road[1], t, n, visited)

            if result != (counter - 1):
                output(1)

# Default case:
output(2)
