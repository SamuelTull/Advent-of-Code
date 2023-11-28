import sys
from collections import defaultdict, deque

DAY = 23
PART = 1

data = str(DAY)
if True:  # change for test data debugging
    data = str(DAY) + "test1"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

S = set()
lines = data.split("\n")
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == "#":
            S.add((r, c))

check = {
    0: [(-1, -1), (-1, 1), (-1, 0)],
    1: [(1, -1), (1, 1), (1, 0)],
    2: [(-1, -1), (1, -1), (0, -1)],
    3: [(-1, 1), (1, 1), (0, 1)],
}

for rID in range(100000):
    moving = defaultdict(set)
    newS = set()
    for r, c in S:
        proposed = foundone = False
        for dID in range(4):
            for dr, dc in check[(rID + dID) % 4]:
                if (r + dr, c + dc) in S:
                    foundone = True
                    break
            else:
                if not proposed:
                    proposed = (r + dr, c + dc)

            if foundone and proposed:
                moving[proposed].add((r, c))
                break
        else:
            newS.add((r, c))

    for (r, c), oldpos in moving.items():
        if len(oldpos) == 1:
            newS.add((r, c))
        else:
            newS |= oldpos

    if rID == 9:
        r0 = min(s[0] for s in S)
        r1 = max(s[0] for s in S)
        c0 = min(s[1] for s in S)
        c1 = max(s[1] for s in S)
        print("P1", (r1 - r0 + 1) * (c1 - c0 + 1) - len(S))

    if S == newS:
        print("P2", rID + 1)
        break
    S = newS


"""check = [
    [[(-1, -1), (-1, 1), (-1, 0)], [(1, -1), (1, 1), (1, 0)], [(-1, -1), (1, -1), (0, -1)],[(-1, 1), (1, 1), (0, 1)]],
    [[(1, -1), (1, 1), (1, 0)],[(-1, -1), (1, -1), (0, -1)], [(-1, 1), (1, 1), (0, 1)], [(-1, -1), (-1, 1), (-1, 0)]],
    [[(-1, -1), (1, -1), (0, -1)],[(-1, 1), (1, 1), (0, 1)], [(-1, -1), (-1, 1), (-1, 0)],[(1, -1), (1, 1), (1, 0)]],
    [[(-1, 1), (1, 1), (0, 1)], [(-1, -1), (-1, 1), (-1, 0)], [(1, -1), (1, 1), (1, 0)], [(-1, -1), (1, -1), (0, -1)]],
]"""
