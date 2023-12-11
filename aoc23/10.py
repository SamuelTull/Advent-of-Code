import sys
from collections import deque

data = "10.txt"
# data = "10test.txt"
if len(sys.argv) > 1:
    data = f"10{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")
R = len(lines)
C = len(lines[0].strip())
G = {}
S = (0, 0)

neigh = lambda r, c: [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]


def connecting_pipes(r, c):
    s = G.get((r, c), None)
    if s == "|":
        return [(r - 1, c), (r + 1, c)]
    if s == "-":
        return [(r, c - 1), (r, c + 1)]
    if s == "L":
        return [(r - 1, c), (r, c + 1)]
    if s == "J":
        return [(r - 1, c), (r, c - 1)]
    if s == "7":
        return [(r + 1, c), (r, c - 1)]
    if s == "F":
        return [(r + 1, c), (r, c + 1)]
    else:
        return []


for r in range(R):
    for c in range(C):
        if lines[r][c] != ".":
            G[(r, c)] = lines[r][c]
            if lines[r][c] == "S":
                S = (r, c)
STARTS = neigh(*S)

cycle = False
for start in STARTS:
    this = [S, start]
    while not cycle:
        n1, n2 = connecting_pipes(*this[-1])
        if this[-2] == n1:
            this.append(n2)
        elif this[-2] == n2:
            this.append(n1)
        else:
            break
        if this[-1] == S:
            cycle = this
print(len(cycle) // 2)  # round down as S in there twice


# Remove all junk that is not part of the cycle
for r, c in G.copy():
    if (r, c) not in cycle:
        del G[(r, c)]


ll, rr = cycle[1], cycle[-2]  # either side of S
assert rr == (ll[0] - 1, ll[1] + 1), f"{rr} {ll}"  # may have to change for test inputs
G[S] = "F"


# make every (r,c) into 2x2 square
# A B
# C D
# if (r,c) in G add A
# if (r,c) connected to (r,c+1) add B
# if (r,c) connected to (r+1,c) add C
# D always empty - beware of 1x1 regions created

walls = set()
for r, c in G:
    walls.add((r * 2, c * 2))
    this, right, below = G.get((r, c), ""), G.get((r, c + 1), ""), G.get((r + 1, c), "")
    if this in "-FL" and right in "-J7":
        walls.add((r * 2, c * 2 + 1))
    if this in "|F7" and below in "|LJ":
        walls.add((r * 2 + 1, c * 2))

# start a flood fill from every point,
# only count the "original points" - those that are at even coordinates
p2 = 0
SEEN = walls
for r in range(2, 2 * R - 2, 2):  # border cannot be inside
    for c in range(2, 2 * C - 2, 2):  # dont count odd coords so skip
        if (r, c) in SEEN:
            continue
        Q = deque([(r, c)])
        escaped = False
        inner = {(r, c)}
        while Q:
            this = Q.popleft()
            for rr, cc in neigh(*this):
                if rr < 0 or rr >= 2 * R or cc < 0 or cc >= 2 * C:
                    escaped = True
                    continue
                if (rr, cc) in SEEN:
                    continue
                SEEN.add((rr, cc))
                Q.append((rr, cc))
                if rr % 2 == 0 and cc % 2 == 0:
                    inner.add((rr, cc))
        if not escaped:
            print(len(inner))  # only 1 inner region, so print as soon as found
