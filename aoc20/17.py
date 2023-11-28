import sys
from collections import defaultdict

DAY = 17
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
S = set()
for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == "#":
            S.add((r, c, 0))

# If a cube is active and exactly 2 or 3 of its neighbors
# are also active, the cube remains active.
# Otherwise, the cube becomes inactive.
# If a cube is inactive but exactly 3 of its neighbors are active,
# the cube becomes active. Otherwise, the cube remains inactive.
for i in range(6):
    newS = set()
    x0 = min(x[0] for x in S)
    y0 = min(x[1] for x in S)
    z0 = min(x[2] for x in S)
    x1 = max(x[0] for x in S)
    y1 = max(x[1] for x in S)
    z1 = max(x[2] for x in S)
    for x in range(x0 - 1, x1 + 2):
        for y in range(y0 - 1, y1 + 2):
            for z in range(z0 - 1, z1 + 2):
                if (x, y, z) in S:
                    s = -1
                    for dx in [0, 1, -1]:
                        for dy in [0, 1, -1]:
                            for dz in [0, 1, -1]:
                                if (x + dx, y + dy, z + dz) in S:
                                    s += 1
                    if s in [2, 3]:
                        newS.add((x, y, z))

                else:
                    s = 0
                    for dx in [0, 1, -1]:
                        for dy in [0, 1, -1]:
                            for dz in [0, 1, -1]:
                                if (x + dx, y + dy, z + dz) in S:
                                    s += 1
                    if s == 3:
                        newS.add((x, y, z))
    S = newS

print(len(S))
# groups = data.split("\n\n")
# grid = [[x for x in line.strip()] for line in data.split("\n")]
# lines = [int(x) for x in lines]
# lines = [x.replace("-", ",").split(",") for x in lines]
# lines = [x.split(" ") for x in lines]
