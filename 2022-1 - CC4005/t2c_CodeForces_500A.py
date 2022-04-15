# Nyveon (Eric K)
# T2 CC4005
# Problem A - Aprendiendo el BFS

# Data structure
from collections import defaultdict, deque
neighborhood = defaultdict(set)


def bfs(graph, start, target, size):
    """
    Breadth first search
    """
    visited = [False] * (size + 1)
    visited[start] = True

    queue = deque([start])

    while queue:
        s = queue.popleft()

        for vertex in graph[s]:
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)
                if vertex == target:
                    return True

    return False


# Input
n, t = [int(x) for x in input().split()]
house_powers = [int(x) for x in input().split()]

for index, house_power in enumerate(house_powers):
    neighborhood[index + 1].add(index + 1 + house_power)


# Processing & Output
possible = bfs(neighborhood, 1, t, n)

if possible:
    print("YES")
else:
    print("NO")