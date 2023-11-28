import sys
from collections import defaultdict, deque

DAY = 18
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()


lines = data.split("\n")
points = set()
for line in lines:
    x, y, z = line.split(",")
    x = int(x)
    y = int(y)
    z = int(z)
    points.add((x, y, z))


x0 = min(s[0] for s in points)
x1 = max(s[0] for s in points)
y0 = min(s[1] for s in points)
y1 = max(s[1] for s in points)
z0 = min(s[2] for s in points)
z1 = max(s[2] for s in points)


def neighbours(s):
    x, y, z = s
    return {
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    }


# fmt: off
def outside(s):
    x, y, z = s
    if x < x0:return True
    if x > x1:return True
    if y < y0:return True
    if y > y1:return True
    if z < z0:return True
    if z > z1:return True
    return False
# fmt: on


memo = {}


def contained(s):
    if s in memo:
        return memo[s]
    q = deque({s})
    seen = {s}
    while q:
        curr = q.popleft()
        for s in neighbours(curr) - points - seen:
            if outside(s):
                memo[s] = False
                return False
            seen.add(s)
            q.append(s)
    memo[s] = True
    return True


P1 = 0
P2 = 0
for s in points:
    for neig in neighbours(s):
        if neig not in points:
            P1 += 1
            if not contained(neig):
                P2 += 1

print("P1", P1, "P2", P2)
