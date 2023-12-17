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
    return (dr + dc) // 4


def neighbours(r, c, d, cnt):
    DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neigh = []
    for nd in range(4):
        if nd == d:
            dr, dc = DIR[d]
            if cnt < 10:
                neigh.append((r + dr, c + dc, nd, cnt + 1))
        elif nd % 2 == d % 2:
            # dont turn around
            continue
        elif cnt >= 4:
            dr, dc = DIR[d]
            neigh.append((r + dr, c + dc, nd, 1))
    return neigh


Q = []
heappush(Q, (dist(0, 0), 0, 0, 0, 0, 1))
seen = set()
while Q:
    f, g, r, c, d, cnt = heappop(Q)
    if (r, c) == (R - 1, C - 1):
        if cnt >= 4:
            print(g)
            break
        continue
    if (r, c, d, cnt) in seen:
        continue
    seen.add((r, c, d, cnt))
    for nr, nc, nd, ncnt in neighbours(r, c, d, cnt):
        if 0 <= nr < R and 0 <= nc < C:
            ng = g + G[nr][nc]
            nf = ng + dist(nr, nc)
            heappush(Q, (nf, ng, nr, nc, nd, ncnt))

# 5.1s
# 4.7s replacing dist function with 0
