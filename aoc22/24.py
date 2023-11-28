import sys
from collections import defaultdict, deque

DAY = 24
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()
data = [[x for x in line.strip()] for line in data.split("\n")]

H = len(data)
W = len(data[0])
assert data[0][1] == "."
assert data[H - 1][W - 2] == "."


bliz = [[], [], [], []]
blizzards = {}
for r in range(1, H - 1):
    for c in range(1, W - 1):
        if data[r][c] == "^":
            bliz[0].append((r, c))
        elif data[r][c] == ">":
            bliz[1].append((r, c))
        elif data[r][c] == "v":
            bliz[2].append((r, c))
        elif data[r][c] == "<":
            bliz[3].append((r, c))

start = (0, 1)
end = (H - 1, W - 2)


def draw_walls(t):
    print("Print Bliz", t)
    for r in range(H):
        print("".join("#" if (r, c) in blizzards[t] else "." for c in range(W)))


def h(pos):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])


def updateblizzards():
    bliz[0] = [(r - 1, c) if r - 1 != 0 else (H - 2, c) for (r, c) in bliz[0]]
    bliz[1] = [(r, c + 1) if c + 1 != W - 1 else (r, 1) for (r, c) in bliz[1]]
    bliz[2] = [(r + 1, c) if r + 1 != H - 1 else (1, c) for (r, c) in bliz[2]]
    bliz[3] = [(r, c - 1) if c - 1 != 0 else (r, W - 2) for (r, c) in bliz[3]]
    blizzards[T] = set(bliz[0] + bliz[1] + bliz[2] + bliz[3])


T = 0
Q = [(start[0], start[1], 0, h(start))]
SEEN = defaultdict(set)
while Q:
    Q.sort(key=lambda x: x[3], reverse=True)
    r, c, t, _ = this = Q.pop()
    if t + 1 > T:
        T = t + 1
        print(T, len(Q), sum(len(S) for S in SEEN.values()))
        updateblizzards()

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]:
        thisnew = (r + dr, c + dc, t + 1)
        if (r + dr, c + dc) == end:
            print("P1", t + 1)
            Q = False
            break
        elif (1 <= r + dr <= H - 2 and 1 <= c + dc <= W - 2) or (
            r + dr,
            c + dc,
        ) == start:
            if (r + dr, c + dc) in blizzards[t + 1]:
                continue
            if (r + dr, c + dc) in SEEN[t + 1]:
                continue
            SEEN[t + 1].add((r + dr, c + dc))
            Q.append((r + dr, c + dc, t + 1, h((r + dr, c + dc)) + t + 1))
