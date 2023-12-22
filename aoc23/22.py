import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])

data = "22.txt"
# data = "22test.txt"
if len(sys.argv) > 1:
    data = f"22{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")


bricks = []
for line in lines:
    x, y, z, x2, y2, z2 = [int(x) for x in line.replace("~", ",").split(",")]
    x, x2 = min(x, x2), max(x, x2)
    y, y2 = min(y, y2), max(y, y2)
    z, z2 = min(z, z2), max(z, z2)
    bricks.append([x, y, z, x2, y2, z2])
bricks.sort(key=lambda x: x[2])

N = len(bricks)


def intercepts(i, j):
    ix, iy, iz, ix2, iy2, iz2 = bricks[i]
    jx, jy, jz, jx2, jy2, jz2 = bricks[j]
    x_intercept = (ix <= jx <= ix2) or (jx <= ix <= jx2)
    y_intercept = (iy <= jy <= iy2) or (jy <= iy <= jy2)
    return x_intercept and y_intercept


for i in range(N):
    dz = bricks[i][2] - 1
    for j in range(i - 1, -1, -1):
        if intercepts(i, j):
            dz = min(dz, bricks[i][2] - bricks[j][5] - 1)
    bricks[i][2] -= dz
    bricks[i][5] -= dz


supports = defaultdict(set)  # k supports all v
supported_by = defaultdict(set)  # k is supported by all v
for i in range(N):
    for j in range(N):
        if intercepts(i, j) and bricks[i][5] + 1 == bricks[j][2]:
            supports[i].add(j)
            supported_by[j].add(i)


p1 = 0
p2 = 0
for i in range(N):
    Q = deque([i])
    falling = {i}
    while Q:
        i = Q.popleft()
        for j in supports[i]:
            if supported_by[j] <= falling:  # subset (all supported by are falling)
                falling.add(j)
                Q.append(j)

    if len(falling) == 1:
        p1 += 1
    else:
        p2 += len(falling) - 1

print("Part 1:", p1)
print("Part 2:", p2)
