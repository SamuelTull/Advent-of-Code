import sys
from collections import defaultdict, deque

DAY = 24
PART = 2

data = str(DAY)
if True:  # change for test data debugging
    data = str(DAY) + "test1"
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

walls = (
    set((0, c) for c in range(W))
    | set((H - 1, c) for c in range(W))
    | set((r, 0) for r in range(H))
    | set((r, W - 1) for r in range(H))
)
walls.remove((0, 1))
walls.add((-1, 1))
walls.remove((H - 1, W - 2))
walls.add((H, W - 2))


def updateblizzards():
    bliz[0] = [(r - 1, c) if r - 1 != 0 else (H - 2, c) for (r, c) in bliz[0]]
    bliz[1] = [(r, c + 1) if c + 1 != W - 1 else (r, 1) for (r, c) in bliz[1]]
    bliz[2] = [(r + 1, c) if r + 1 != H - 1 else (1, c) for (r, c) in bliz[2]]
    bliz[3] = [(r, c - 1) if c - 1 != 0 else (r, W - 2) for (r, c) in bliz[3]]


def add(r, c, state, t):
    if (r, c, state) not in SEEN:
        SEEN.add((r, c, state))
        Q.append((r, c, state, t))


# r,c,state,h
# state = 0 -> going to end
# state = 1 -> back to start
# state = 2 -> back to goal
Q = deque([(0, 1, 0, 0)])
T = -1
while Q:
    r, c, state, t = Q.popleft()
    if t > T:
        print(t, len(Q))
        T = t
        updateblizzards()
        blizzards = set(bliz[0] + bliz[1] + bliz[2] + bliz[3]) | walls
        SEEN = set()
    if r == H - 1:
        if state == 2:
            print("P2", t)
            break
        else:
            state = 1
    elif r == 0 and state == 1:
        state = 2

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]:
        thisnew = (r + dr, c + dc, t + 1)
        if (r + dr, c + dc) not in blizzards:
            add(r + dr, c + dc, state, t + 1)
