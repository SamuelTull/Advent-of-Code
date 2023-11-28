import sys
from collections import defaultdict

DAY = 12
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
x = y = 0
heading = "E"
turnLeft = {"E": "N", "N": "W", "W": "S", "S": "E"}
turnRight = {"E": "S", "S": "W", "W": "N", "N": "E"}
D = {"E": (-1, 0), "N": (0, -1), "W": (1, 0), "S": (0, 1)}
V = set()
for line in lines:
    print(x, y, heading)
    print()
    print(line)
    ins = line[0]
    val = int(line[1:])
    dx = dy = 0
    if ins == "L":
        for _ in range(val // 90):
            heading = turnLeft[heading]
    elif ins == "R":
        for _ in range(val // 90):
            heading = turnRight[heading]
    elif ins == "F":
        dx, dy = D[heading]
    else:
        dx, dy = D[ins]
    x += val * dx
    y += val * dy

print(x, y)
print(abs(x) + abs(y))
