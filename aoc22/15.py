import sys
from collections import defaultdict

DAY = 15
PART = 1
r = 2000000
MAX = 4000000
data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
    r = 10
    MAX = 20
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
    r = 10
    MAX = 20
with open(data + ".txt") as f:
    data = f.read().strip()


lines = data.split("\n")
S = []
M = set()
for line in lines:
    line = line.replace(":", " ").replace("=", " ").replace(",", " ").split(" ")
    x1, y1, x2, y2 = int(line[3]), int(line[6]), int(line[13]), int(line[16])
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    d = dx + dy
    S.append([x1, y1, d])
    dd = abs(r - y1)
    if dd < d:
        for xx in range(x1 - d + dd, x1 + d - dd + 1):
            if (xx, r) != (x1, y1) and (xx, r) != (x2, y2):
                M.add((xx, r))
print("P1", len(M))


def valid(newX, newY):
    for sx, sy, d in S:
        if abs(newX - sx) + abs(newY - sy) <= d:
            return False
    return True


for sx, sy, d in S:
    print("P2 Searching", sx, sy)
    d = d + 1  # look at all the values d+1 away
    for dirx, diry in ((1, 1), (-1, 1), (-1, -1), (1, -1)):
        newX = sx + dirx * d
        newY = sy
        i = 0
        while 0 <= newX <= MAX and 0 <= newY <= MAX and i <= d:
            if valid(newX, newY):  # dont save all and check later check now!!
                print(f"P2 Found, {(newX, newY)}, {(newX*4000000 + newY)} ")
            newX -= dirx
            newY += diry
            i += 1
