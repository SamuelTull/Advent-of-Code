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


sr = 0
sc = G[0].index(".")
OPEN = [(sr, sc, set())]

p1 = -1


def neigh(r, c):
    if G[r][c] == ".":
        out = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
    elif G[r][c] == ">":
        out = [(r, c + 1)]
    elif G[r][c] == "<":
        out = [(r, c - 1)]
    elif G[r][c] == "^":
        out = [(r - 1, c)]
    elif G[r][c] == "v":
        out = [(r + 1, c)]
    else:
        assert False
    return [(r, c) for r, c in out if 0 <= r < R and 0 <= c < C and G[r][c] != "#"]


while OPEN:
    r, c, SEEN = OPEN.pop()
    if r == R - 1:
        p1 = max(p1, len(SEEN))
        continue
    for nr, nc in neigh(r, c):
        if (nr, nc) not in SEEN:
            OPEN.append((nr, nc, SEEN | {(nr, nc)}))


print(p1)
