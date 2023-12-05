import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)


def neighbours(pt):
    r, c = pt
    out = []
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if 0 == dr == dc:
                continue
            if 0 <= r + dr < R and 0 <= c + dr < C:
                out.append((r + dr, c + dc))
    return out


data = "3.txt"
# data = "3test.txt"
if len(sys.argv) > 1:
    data = f"3{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

G = []
P1 = set()  # all neighbours of symbols- combined
P2 = []  # all neighbours of * - separate

lines = data.split("\n")
R = len(lines)
C = len(lines[0])
for r in range(R):
    c = 0
    while c + 1 < C:
        if lines[r][c] in "0123456789":
            num = lines[r][c]
            pts = [(r, c)]
            while c + 1 < C and lines[r][c + 1] in "0123456789":
                num += lines[r][c + 1]
                pts.append((r, c + 1))
                c += 1
            G.append((int(num), pts))
        elif lines[r][c] != ".":
            neigh = neighbours((r, c))
            for ri, ci in neigh:
                P1.add((ri, ci))
            if lines[r][c] == "*":
                P2.append(neigh)
        c += 1

s = 0
for num, pts in G:
    if set(pts) & P1:
        s += num
print(s)

s = 0
for neigh in P2:  # all *
    neigh = set(neigh)
    count = 0
    curr = 1
    for num, pts in G:
        if neigh & set(pts):
            if count == 2:  # > 2
                break
            count += 1
            curr *= num
    else:  # no break
        if count == 2:
            s += curr
print(s)
