import sys
from collections import defaultdict, deque

DAY = 18
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
points = set()
for line in lines:
    x, y, z = line.split(",")
    x = int(x)
    y = int(y)
    z = int(z)
    points.add((x, y, z))

x0 = min(s[0] for s in points)
x1 = max(s[0] for s in points)
y0 = min(s[1] for s in points)
y1 = max(s[1] for s in points)
z0 = min(s[2] for s in points)
z1 = max(s[2] for s in points)


def neighbours(s):
    x, y, z = s
    return {
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    }


q = deque([(x0 - 1, y0 - 1, z0 - 1)])
seen = {(x0 - 1, y0 - 1, z0 - 1)}
outside = {(x0 - 1, y0 - 1, z0 - 1)}
while q:
    s = q.popleft()
    for x, y, z in neighbours(s):
        if (
            x < x0 - 1
            or x > x1 + 1
            or y < y0 - 1
            or y > y1 + 1
            or z < z0 - 1
            or z > z1 + 1
        ):
            continue
        if (x, y, z) not in outside | points:
            q.append((x, y, z))
            outside.add((x, y, z))

inside = {
    (x, y, z)
    for x in range(x0, x1 + 1)
    for y in range(y0, y1 + 1)
    for z in range(z0, z1 + 1)
} - outside


P2 = 0
for s in inside:
    for neig in neighbours(s):
        if neig not in inside:
            P2 += 1

print("P2", P2)
