import sys
from collections import defaultdict

DAY = 8
PART = 1, 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
possible = []
for i in range(len(lines)):
    x1, x2 = lines[i].strip().split(" ")
    x2 = eval(x2)
    lines[i] = [x1, x2]


visited = []
idx = a = 0
while idx not in visited:
    visited.append(idx)
    x1, x2 = lines[idx]
    if x1 == "acc":
        a += x2
        idx += 1
    elif x1 == "jmp":
        idx += x2
    else:
        idx += 1
print("P1", a)


for i in range(len(lines) - 1, -1, -1):  # seemed more likely to be near bottom
    old = lines[i]
    if old[0] != "acc":
        lines[i] = [{"jmp": "nop", "nop": "jmp"}[old[0]], old[1]]
        visited = []
        idx = a = 0
        loop = True
        while idx not in visited:
            if idx >= len(lines):
                loop = False
                break
            visited.append(idx)
            x1, x2 = lines[idx]
            if x1 == "acc":
                a += x2
                idx += 1
            elif x1 == "jmp":
                idx += x2
            else:
                idx += 1

        if not loop:
            print("P2", a)
            break

        lines[i] = old
