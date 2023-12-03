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

Gn = []
Gs = {}
lines = data.split("\n")
R = len(lines)
C = len(lines[0])
for r in range(R):
    c = 0
    while c < C:
        if lines[r][c] not in "0123456789.":
            Gs[(r, c)] = lines[r][c]
        elif lines[r][c] != ".":
            num = lines[r][c]
            pts = [(r, c)]
            while c + 1 < C and lines[r][c + 1] in "0123456789":
                num += lines[r][c + 1]
                pts.append((r, c + 1))
                c += 1
            Gn.append((int(num), pts))
        else:
            assert lines[r][c] == ".", lines[r][c]
        c += 1


def neighbours(pt):
    r, c = pt
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if 0 == dr == dc:
                continue
            if 0 <= r + dr < R and 0 <= c + dr < C:
                yield (r + dr, c + dc)


# s = 0

# for pt in Gs:
#     for r, c in neighbours(pt):
#         for i in range(len(Gn) - 1, -1, -1):
#             (num, pts) = Gn[i]
#             if (r, c) in pts:
#                 s += num
#                 del Gn[i]
# print(s)

s = 0
for pt, val in Gs.items():
    if val != "*":
        continue
    neigh = {}
    for r, c in neighbours(pt):
        for i in range(len(Gn)):
            num, pts = Gn[i]
            if (r, c) in pts:
                neigh[i] = num

    if len(neigh) == 2:
        curr = 1
        for num in neigh.values():
            curr *= num

        s += curr
print(s)
