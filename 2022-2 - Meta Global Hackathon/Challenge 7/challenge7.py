# Eric K.
# Meta Global Hackathon 2022

# Imports
from numba import jit
import numpy as np

# Constants
inf = float("inf")
width, height, floors = int(0), int(0), int(0)


# Floyd wqarshall for a single floor of the graph
@jit(nopython=True)
def floyd_warshall(graph):
    dist = graph
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist


# Print the distances on the same floor for the given x, y
def print_distance_field(dist, x, y):
    for h in range(width):
        for w in range(width):
            a = dist[y*width+x][h*width+w]
            if a == float("inf"):
                a = "##"
            else:
                a = "{:.0f}".format(a).zfill(2)
            print(a, end=",")
        print()


# Build the adjacency matrix for the graph
def build_matrix(lines, floors):
    adj = [[[inf for x in range(width*height)]
            for y in range(width*height)]
           for _ in range(floors)]
    adj = np.array(adj, dtype=np.float64)
    employees = [set() for _ in range(floors)]
    stairs = [(-1, -1) for _ in range(floors)]

    for floor in range(floors):
        for y in range(height):
            for x in range(width):
                if lines[y][x] == "." or lines[y][x] == "s"\
                        or lines[y][x] == "o":
                    if y > 0 and\
                            (lines[y-1][x] == "." or lines[y-1][x] == "s"):
                        adj[floor][y*width+x][(y-1)*width+x] = 1
                    if y < height-1 and\
                            (lines[y+1][x] == "." or lines[y+1][x] == "s"):
                        adj[floor][y*width+x][(y+1)*width+x] = 1
                    if x > 0 and\
                            (lines[y][x-1] == "." or lines[y][x-1] == "s"):
                        adj[floor][y*width+x][y*width+x-1] = 1
                    if x < width-1 and\
                            (lines[y][x+1] == "." or lines[y][x+1] == "s"):
                        adj[floor][y*width+x][y*width+x+1] = 1
                    if lines[y][x] == "s":
                        stairs[floor] = (x, y)
                    if lines[y][x] == "o":
                        employees[floor].add((x, y))
        lines = lines[height+1:]

    return (adj, employees, stairs)


# Distance to a point on the same floor
def distance_to_point(distances, x1, y1, x2, y2, f):
    return distances[f][y1 * width + x1][y2 * width + x2]


def d_to_point_via_stairs(distances, stairs, x1, y1, x2, y2, f1, f2):
    """Calculates the distance from one point to another, traversing floors

    If point A is on floor 0, and point B is on floor 1, then the distance
    is the distance from A to the stairs, plus the distance from the stairs
    to B.

    Args:
        distances: The floyd-warshall calculation per floor
        stairs: The stairs per floor
        x1, y1, f1: The coordinates of the first point. (f1 is floor)
        x2, y2, f2: The coordinates of the second point. (f2 is floor)
    """

    # Same floor
    if f1 == f2:
        return distance_to_point(distances, x1, y1, x2, y2, f1)
    else:
        s1x, s1y = stairs[f1]
        s2x, s2y = stairs[f2]
        p1_to_s1 = distance_to_point(distances, x1, y1, s1x, s1y, f1)
        s2_to_p2 = distance_to_point(distances, s2x, s2y, x2, y2, f2)
        return p1_to_s1 + s2_to_p2
    # Output
    return 0


# Minimum sum of distances to all employeed
def distance_to_employees(current_min, distances, employees, stairs, x, y, f):
    """Calculates the distance to all employees from this point

    Args:
        current_min: The current minimum distance, for culling reasons
        distances: The floyd-warshall calculation per floor
        employees: The set of employees per floor
        x, y, f: The coordinated of the point to query. (f is floor)
    """

    # Same floor
    current_sum = 0
    for floor in range(floors):
        for employee in employees[floor]:
            ex, ey = employee
            distance = d_to_point_via_stairs(distances,
                                             stairs, ex, ey,
                                             x, y, floor, f)
            current_sum += distance
            if current_sum > current_min:
                return inf

    # Output
    return current_sum


def main():
    # Input
    lines, ans_lines = [], []
    files = [
        "mini_test.txt",
        "test_input.txt",
        "micro_kitchens_hard_input.txt"]
    with open(files[2], "r") as f:
        for line in f:
            lines.append(line.rstrip())

    # Input Processing
    global width, height, floors
    width, height, floors = [int(x) for x in lines[0].split()]
    lines = lines[1:]
    for i in range(len(lines)):
        lines[i] = [x for x in lines[i].split()]
    adjacency, employees, stairs = build_matrix(lines, floors)

    print("Input processed.\nCalculating distance fields:")

    # Adjacency field for each floor
    distances = []
    for floor in range(floors):
        print(f"Floor {floor + 1}/{floors}")
        distances.append(floyd_warshall(adjacency[floor]))

    print("Done.\nCalculating minimum distance:")
    # Distance to employees
    min_distance = inf
    candidates = []
    for floor in range(floors):
        print(f"Floor {floor + 1}/{floors}")
        for y in range(height):
            print(f"{y+1}/{height}")
            for x in range(width):
                if (x, y) != stairs[floor] and (x, y) not in employees[floor]:
                    distance = distance_to_employees(min_distance,
                                                     distances, employees,
                                                     stairs, x, y, floor)
                    if distance < min_distance:
                        min_distance = distance
                        candidates = [(floor, x, y)]
                    elif distance == min_distance:
                        candidates.append((floor, x, y))
        print("=======")
    print(min_distance)

    # Sort candidates lexographically
    candidates.sort(key=lambda x: (x[0], x[1], x[2]))

    # Print candidates on same line
    for candidate in candidates:
        # print(f"({candidate[0]}, {candidate[1]}, {candidate[2]})", end=" ")
        ans_lines.append(f"({candidate[0]}, {candidate[1]}, {candidate[2]})")

    # Output
    with open("out.txt", "w") as f:
        for line in ans_lines:
            f.write(line + " ")


if __name__ == "__main__":
    main()
