import sys
from collections import defaultdict, deque

DAY = 3
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

wires = data.split("\n")
for i in range(2):
    S = set((0, 0))
    cx, cy = 0, 0
    for instr in wires[i].split(","):
        dx = {"R": 1, "L": -1, "U": 0, "D": 0}[instr[0]]
        dy = {"R": 0, "L": 0, "U": 1, "D": -1}[instr[0]]
        for _ in range():
            cx += dx
            cy += dy
            S.add((cx, cy))
    wires[i] = S

intersect = wires[0] & wires[1]
best = 1e10
for x, y in intersect:
    if x + y < best:
        best = x + y
print(x + y)
