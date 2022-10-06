# Eric K.
# Meta Global Hackathon 2022

from collections import defaultdict

# Input
lines = []
# file_name = "test_input.txt"
file_name = "ci_pipelines_hard_input.txt"
with open(file_name, "r") as f:
    for line in f:
        lines.append(line.rstrip())

# Processing
N = int(lines[0])
lines = lines[2:]

capacities = []
for i in range(N):
    capacities.append(int(lines[i]))
lines = lines[N+1:]

graph = defaultdict(list)
while True:
    # If end of lines
    if len(lines) == 0:
        break

    a, b = [int(x) for x in lines[0].split()]
    graph[a].append(b)
    lines = lines[1:]

Inf = float('inf')
N += 2

# Convert graph to flow network
flow_network = defaultdict(list)
for node in graph:
    flow_network[node] = [(node + N, capacities[node])]
    flow_network[node + N] = []

for node in graph:
    for edge in graph[node]:
        flow_network[node + N].append((edge, Inf))

# Find all nodes that have no incoming edges
roots = set()
for node in flow_network:
    roots.add(node)

for node in flow_network:
    for edge in flow_network[node]:
        roots.discard(edge[0])

# Find all nodes that have no outgoing edges
leaves = set()
for node in graph:
    for edge in graph[node]:
        leaves.add(edge)

for node in graph:
    leaves.discard(node)

# Add start node that points to all roots
start = N*2 + 1
flow_network[start] = [(x, Inf) for x in roots]

# Add end node that is pointed to by all leaves
end = N*2 + 2
for leaf in leaves:
    flow_network[leaf] = [(end, capacities[leaf])]

# Convert to adjacency matrix with default 0
adj_matrix = [[0 for i in range(N*2 + 3)] for j in range(N*2 + 3)]
for node in flow_network:
    for edge in flow_network[node]:
        adj_matrix[node][edge[0]] = edge[1]


# Find max flow using adjacency matrix
def bfs(rGraph, s, t, parent):
    visited = [False] * (N*2 + 3)
    queue = []
    queue.append(s)
    visited[s] = True

    while queue:
        u = queue.pop(0)

        for ind, val in enumerate(rGraph[u]):
            if visited[ind] is False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[t] else False


def fordFulkerson(graph, source, sink):
    parent = [-1] * (len(graph))
    max_flow = 0

    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while (s != source):
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while (v != source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


print(fordFulkerson(adj_matrix, start, end))

# Output
ans = ''
with open("out.txt", "w") as f:
    f.write(ans)
