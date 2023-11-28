import sys
from collections import defaultdict, deque

DAY = 5
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
points = defaultdict(int)


def print_points(points):
    max_x = max(x for x, y in points.keys())
    max_y = max(y for x, y in points.keys())
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            print(points[(x, y)], end="")
        print()


for line in lines:
    p1, p2 = line.split("->")
    x1, y1 = [int(x) for x in p1.split(",")]
    x2, y2 = [int(x) for x in p2.split(",")]

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points[(x, y1)] += 1

    else:
        dx = x2 - x1
        dy = y2 - y1
        sx = 1 if dx > 0 else -1
        sy = 1 if dy > 0 else -1
        dx = abs(dx)
        dy = abs(dy)
        assert dx == dy
        for i in range(dx + 1):
            points[(x1 + i * sx, y1 + i * sy)] += 1

    # print(x1, y1, x2, y2)
    # print_points(points)

print(sum(1 for v in points.values() if v > 1))
