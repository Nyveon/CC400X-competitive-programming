# Nyveon (Eric K)
# T2 CC4005
# Problem A - Aprendiendo el BFS

# Data structure
from collections import defaultdict, deque
tree = defaultdict(list)


def get_index(x):
    return indexes[x]


# Input
n = int(input())

for i in range(n - 1):
    a, b = [int(x) for x in input().split()]
    tree[a].append(b)
    tree[b].append(a)

sequence = [int(x) for x in input().split()]

# Processing
indexes = [0]*(n+1)
current_index = 0
for number in sequence:
    indexes[number] = current_index
    current_index += 1

path_validity = True
if len(sequence) != 1:
    for vertex in tree:
        tree[vertex].sort(key=get_index)

    # BFS
    visited = [False] * (n + 1)
    visited[1] = True
    queue = deque([1])
    popped_index = 0

    while queue:
        s = queue.popleft()
        if sequence[popped_index] != s:
            path_validity = False
            break
        popped_index += 1

        for vertex in tree[s]:
            if not visited[vertex]:
                visited[vertex] = True
                queue.append(vertex)


# Output
if path_validity:
    print("Yes")
else:
    print("No")
