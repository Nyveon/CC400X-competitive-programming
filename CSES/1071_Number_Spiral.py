# Eric K
# 22/03/2023


def find_on_spiral(x, y):
    if x > y:
        spiral = x
        if x % 2 == 0:
            spiral_first = (spiral - 1)**2
            return spiral_first + y
        else:
            spiral_first = spiral**2
            return spiral_first - y + 1
    else:
        spiral = y
        if y % 2 == 0:
            spiral_first = spiral**2
            return spiral_first - x + 1
        else:
            spiral_first = (spiral - 1)**2
            return spiral_first + x


t = int(input())

for _ in range(t):
    y, x = [int(x) for x in input().split()]
    print(find_on_spiral(x, y))
