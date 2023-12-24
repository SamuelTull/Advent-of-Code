import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])

data = "23.txt"
# data = "23test.txt"
if len(sys.argv) > 1:
    data = f"23{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

G = data.split("\n")
R = len(G)
C = len(G[0])


def neigh(r, c):
    out = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    return [(r, c) for r, c in out if 0 <= r < R and 0 <= c < C and G[r][c] != "#"]


nodes = []
Q = deque()
for r in range(R):
    for c in range(C):
        if G[r][c] == "." and len(neigh(r, c)) != 2:
            nodes.append((r, c))
            Q.append((r, c, len(nodes) - 1, 0))

seen = set()
adj = defaultdict(dict)  # connections and distances

while Q:
    r, c, i, d = Q.pop()
    seen.add((r, c))
    for nr, nc in neigh(r, c):
        if (nr, nc) in nodes:
            j = nodes.index((nr, nc))
            if i != j:
                adj[i][j] = d + 1
                adj[j][i] = d + 1
        elif (nr, nc) not in seen:
            Q.append((nr, nc, i, d + 1))


start = 0
end = len(nodes) - 1

p2 = -1

Q = deque([(start, 0, 0)])

STATES = defaultdict(int)
STATES[(start, 0)] = -1

while Q:
    x, seen, d = Q.pop()

    if STATES[(x, seen)] >= d:
        continue
    STATES[(x, seen)] = d

    if x == end:
        if d > p2:
            p2 = d
            print(p2, len(Q))
        continue

    for nx, dd in adj[x].items():
        if seen & (1 << nx):
            continue

        nseen = seen | (1 << nx)
        nd = d + dd

        if STATES[(nx, nseen)] >= nd:
            continue
        STATES[(nx, nseen)] = nd - 1

        Q.append((nx, nseen, nd))


print(p2)
