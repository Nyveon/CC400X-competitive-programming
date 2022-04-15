# Nyveon (Eric K)
# T2 CC4005
# Problem B - Mi ciclo querido

# Data structure
from collections import defaultdict

graph = defaultdict(set)


# Input
n, m, k = [int(x) for x in input().split()]

for line in range(m):
    a, b = [int(x) for x in input().split()]
    graph[a].add(b)
    graph[b].add(a)

# Processing
path = [1]
visited = [False] * (max(graph) + 1)
visited[1] = True
while True:
    current = path[-1]
    found = False
    for vertex in graph[current]:
        if not visited[vertex]:
            visited[vertex] = True
            path.append(vertex)
            found = True
            break
    if not found:
        break

vf = path[-1]
for index, number in enumerate(path):
    if vf in graph[number]:
        path = path[index::]
        break

# Output
print(len(path))
for number in path:
    print(number, end=" ")
