import sys
from collections import defaultdict

DAY = 3
PART = 1 + 2
data = str(DAY)

if len(sys.argv) > 1:
    if sys.argv[1] in ["0", "test"]:
        data = str(DAY) + "test"
    else:
        data = str(DAY) + sys.argv[1]

with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
W = len(lines[0])
H = len(lines)
S = set()
for y in range(H):
    for x in range(W):
        if lines[y][x] == "#":
            S.add((x, y))

C = 1
for dx, dy in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
    c = 0
    x, y = (0, 0)
    while y < H:
        if (x % W, y) in S:
            c += 1
        x += dx
        y += dy
    if (dx, dy) == (3, 1):
        print("p1", c)
    C *= c
print("p2", C)
