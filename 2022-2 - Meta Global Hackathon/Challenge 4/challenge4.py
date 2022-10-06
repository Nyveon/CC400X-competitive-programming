# Eric K.
# Meta Global Hackathon 2022

from heapq import heappush, heappop

# Input
lines = []
# file_name = "test_input.txt"
file_name = "commercial_operations_hard_input.txt"
with open(file_name, "r") as f:
    for line in f:
        lines.append(line.rstrip())

# Processing

# Step 1: Make a graph form the inputs
# Step 2: Dijkstra function where weights are edited by time
# Step 3: Binary search for the time

# Number of nodes, number of edges
N, M = [int(x) for x in lines[0].split()]
lines = lines[1:]
print()

# Adjacency list, where weights have two values: c and d
adjacency = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c, d = [int(x) for x in lines[i].split()]
    adjacency[a].append((b, c, d))
    adjacency[b].append((a, c, d))


def get_edge_weight(a, b, t):
    return (a*t + b)


def dijkstra(graph, start, t):
    """
        Uses Dijkstra's algortihm to find the shortest path from node start
        to all other nodes in a directed weighted graph.
    """
    n = len(graph)
    dist, parents = [float("inf")] * n, [-1] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len == dist[v]:
            for c, d, e in graph[v]:
                if dist[c] > path_len + get_edge_weight(d, e, t):
                    dist[c] = path_len + get_edge_weight(d, e, t)
                    parents[c] = v
                    heappush(queue, (dist[c], c))

    return dist, parents


# Make a graph the longest path over time using pyplot
"""
import matplotlib.pyplot as plt
import numpy as np
# Make a list of times
times = np.linspace(0, 1440, 600)
# Make a list of shortest paths
shortest_paths = []
for t in times:
    print(t)
    shortest_paths.append(dijkstra(adjacency, 1, t)[0][N])
# Plot the shortest paths
plt.plot(times, shortest_paths)
plt.show()
"""

# Find the global maxima efficiently
left = 0
right = 1440
while right - left > 0.0000001:
    mid = (left + right) / 2
    if dijkstra(adjacency, 1, mid)[0][N] \
            < dijkstra(adjacency, 1, mid + 0.0000001)[0][N]:
        left = mid
    else:
        right = mid

# Output
ans = dijkstra(adjacency, 1, right)[0][N]
ans = str(round(ans, 5))
print(left, ans)
with open("out.txt", "w") as f:
    f.write(ans + '\n')
