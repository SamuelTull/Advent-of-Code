import sys
from collections import defaultdict, deque

DAY = 13
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

points, instructions = data.split("\n\n")
points = points.split("\n")
instructions = instructions.split("\n")

points = set(tuple(map(int, point.split(","))) for point in points)


def print_points(points):
    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


p1 = None
for line in instructions:
    new_points = set()
    xy, val = line.split()[-1].split("=")
    val = int(val)
    if xy == "x":
        for point in points:
            if point[0] < val:
                new_points.add(point)
            else:
                new_points.add((2 * val - point[0], point[1]))
    else:
        for point in points:
            if point[1] < val:
                new_points.add(point)
            else:
                new_points.add((point[0], 2 * val - point[1]))
    if p1 is None:
        p1 = len(new_points)

    points = new_points


print(p1)
