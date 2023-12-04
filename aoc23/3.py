import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

data = "3.txt"
# data = "3test.txt"
if len(sys.argv) > 1:
    data = f"3{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

G = []
P1 = set()
P2 = {}

lines = data.split("\n")
R = len(lines)
C = len(lines[0])
for r in range(R):
    c = -1
    while c + 1 < C:
        c += 1
        if lines[r][c] == ".":
            continue
        if lines[r][c] in "0123456789":
            num = lines[r][c]
            pts = [(r, c)]
            while c + 1 < C and lines[r][c + 1] in "0123456789":
                num += lines[r][c + 1]
                pts.append((r, c + 1))
                c += 1
            G.append((int(num), pts))
        else:
            P1.add((r, c))
            if lines[r][c] == "*":
                P2[(r, c)] = lines[r][c]


def neighbours(pt):
    r, c = pt
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if 0 == dr == dc:
                continue
            if 0 <= r + dr < R and 0 <= c + dr < C:
                yield (r + dr, c + dc)


s = 0

for pt in P1:
    for r, c in neighbours(pt):
        for i in range(len(G) - 1, -1, -1):
            (num, pts) = G[i]
            if (r, c) in pts:
                s += num
                del G[i]
print(s)

s = 0
for pt, val in Gs.items():
    if val != "*":
        continue
    neigh = {}
    for r, c in neighbours(pt):
        for i in range(len(G)):
            num, pts = G[i]
            if (r, c) in pts:
                neigh[i] = num

    if len(neigh) == 2:
        curr = 1
        for num in neigh.values():
            curr *= num

        s += curr
print(s)
