import sys
from heapq import heappop, heappush

data = "17.txt"
# data = "17test.txt"
if len(sys.argv) > 1:
    data = f"17{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")
G = [[int(x) for x in line] for line in lines]
R = len(G)
C = len(G[0])


def dist(r, c):
    dr = R - 1 - r
    dc = C - 1 - c
    return dr + dc


for part in [1, 2]:
    Q = []
    heappush(Q, (dist(0, 0), 0, 0, 0, 0))
    heappush(Q, (dist(0, 0), 0, 0, 0, 1))
    seen = set()
    while Q:
        f, g, r, c, d = heappop(Q)
        if (r, c) == (R - 1, C - 1):
            print(g)
            break
        if (r, c, d) in seen:
            continue
        seen.add((r, c, d))
        dr, dc = [(0, 1), (1, 0), (0, -1), (-1, 0)][d]
        for cnt in range(10):
            if part == 1 and cnt > 2:
                break
            r += dr
            c += dc
            if r < 0 or r >= R or c < 0 or c >= C:
                break
            g += G[r][c]
            f = g + dist(r, c)
            if (part == 1) or (part == 2 and cnt > 2):
                for nd in range(4):
                    if nd % 2 == d % 2:
                        continue
                    heappush(Q, (f, g, r, c, nd))
