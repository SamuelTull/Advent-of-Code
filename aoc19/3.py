import sys
from collections import defaultdict, deque

DAY = 3
PART = 1


data = str(DAY)
if True:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

wires = list(data.split("\n"))
for i in range(2):
    S = {(0, 0): 0}
    cx, cy = 0, 0
    step = 1
    for instr in wires[i].split(","):
        dx = {"R": 1, "L": -1, "U": 0, "D": 0}[instr[0]]
        dy = {"R": 0, "L": 0, "U": 1, "D": -1}[instr[0]]
        for _ in range(int(instr[1:])):
            cx += dx
            cy += dy
            S[(cx, cy)] = step
            step += 1
    wires[i] = S

intersect = wires[0].keys() & wires[1].keys()
best = 1e10
for x, y in intersect - {(0, 0)}:
    s1 = wires[0][(x, y)]
    s2 = wires[1][(x, y)]
    if s1 + s2 < best:
        best = s1 + s2
print(best)
