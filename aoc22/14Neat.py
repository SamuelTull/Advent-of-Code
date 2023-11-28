import sys
from collections import defaultdict
from utils import defaultlambdadict
from copy import deepcopy

data_dict = defaultlambdadict(
    lambda x: f"test{x}.txt",
    {
        "in": "in.txt",
        "0": "in.txt",
        0: "in.txt",
    },
)

try:
    data = data_dict[sys.argv[1]]
except:
    data = data_dict[1]


with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")

S = set()
for line in lines:
    prev = None
    for point in line.split("->"):
        x, y = point.split(",")
        curr = int(x), int(y)
        if prev != None:
            xp, yp = prev
            x, y = curr
            x, xp = sorted([x, xp])
            y, yp = sorted([y, yp])
            dx = xp - x
            dy = yp - y
            steps = max(dx, dy)
            for i in range(steps + 1):
                S.add(((x + i * (xp > x)), (y + i * (yp > y))))
        prev = curr
START = {s for s in S}

# P1


def print_grid():
    x_min = min(x[0] for x in S)
    x_max = max(x[0] for x in S)
    y_min = min(x[1] for x in S)
    y_max = max(x[1] for x in S)

    print()
    for i in range(y_min, y_max + 1):
        row = [x[0] for x in S if x[1] == i]
        print("".join("#" if x in row else "." for x in range(x_min, x_max + 1)))
    print()


# print_grid()
MAX_DEPTH = max(x[1] for x in S)
C = 0
found = False
while not found:
    s = (500, 0)
    moving = True
    while moving and not found:
        if s[1] > MAX_DEPTH + 1:
            found = True
        elif (s[0], s[1] + 1) not in S:
            s = (s[0], s[1] + 1)
        elif (s[0] - 1, s[1] + 1) not in S:
            s = (s[0] - 1, s[1] + 1)
        elif (s[0] + 1, s[1] + 1) not in S:
            s = (s[0] + 1, s[1] + 1)
        else:
            moving = False
    if not found:
        S.add(s)
        C += 1

# print_grid()
print("P1", C)
##################################
################# P2
##################################
S = START
MAX_DEPTH = max(x[1] for x in S)
for x in range(500 - MAX_DEPTH - 5, 500 + MAX_DEPTH + 5):
    S.add((x, MAX_DEPTH + 2))
# print_grid()
C = 0
found = False
while not found:
    s = (500, 0)
    moving = True
    while moving and not found:
        if (s[0], s[1] + 1) not in S:
            s = (s[0], s[1] + 1)
        elif (s[0] - 1, s[1] + 1) not in S:
            s = (s[0] - 1, s[1] + 1)
        elif (s[0] + 1, s[1] + 1) not in S:
            s = (s[0] + 1, s[1] + 1)
        else:
            moving = False
            if s == (500, 0):
                found = True
    S.add(s)
    C += 1
# print_grid()
print("P2", C)
