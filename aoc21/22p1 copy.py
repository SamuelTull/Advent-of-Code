import sys
import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

DAY = 22
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")


def clip(x1, x2):
    if x1 < -50 and x2 < -50:
        return _, _, True
    if x1 > 50 and x2 > 50:
        return _, _, True
    return max(-50, min(50, x1)), max(-50, min(50, x2)), False


G = [[[False for _ in range(101)] for _ in range(101)] for _ in range(101)]

for line in lines:
    print(len(G))
    line = line.replace(",", " ").replace(".", " ").replace("=", " ")
    on, _, x1, x2, _, y1, y2, _, z1, z2 = line.split()
    on = on == "on"
    x1, x2, outX = clip(int(x1), int(x2))
    y1, y2, outY = clip(int(y1), int(y2))
    z1, z2, outZ = clip(int(z1), int(z2))
    if outX or outY or outZ:
        continue

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(z1, z2 + 1):
                G[x][y][z] = on

print(sum(sum(sum(row) for row in plane) for plane in G))
