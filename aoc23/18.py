import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="()": "".join([x for x in string if x not in chars])

data = "18.txt"
# data = "18test.txt"
if len(sys.argv) > 1:
    data = f"18{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")


def shoelace_area(points):
    # area inside a polygon given its vertices on the plane
    A = sum(
        points[i][1] * points[i - 1][0] - points[i][0] * points[i - 1][1]
        for i in range(len(points))
    )
    return abs(A) / 2


for part in [1, 2]:
    points = [(0, 0)]
    perimeter = 0
    for line in lines:
        d, amt, hexa = line.split()

        if part == 1:
            amt = int(amt)
            dx, dy = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}[d]

        if part == 2:
            amt = int(hexa[2:-2], 16)
            dx, dy = {"3": (0, 1), "1": (0, -1), "2": (-1, 0), "0": (1, 0)}[hexa[-2]]
        x, y = points[-1]
        points.append((x + dx * amt, y + dy * amt))
        perimeter += amt

    # picks theorem:
    # A = area of polygon
    # i = # interior lattice points
    # b = # perimeter lattice points
    #       A = i + b / 2 - 1
    #   i + b = A + b /2 + 1

    print(int(shoelace_area(points) + perimeter / 2 + 1))
