import sys
from collections import defaultdict, deque

DAY = 22
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read()
grid, instr_data = data.split("\n\n")

grid = [[x for x in line] for line in grid.split("\n")]
instructions = []
curr = ""
for char in instr_data:
    if char == "L" or char == "R":
        if curr:
            instructions.append(int(curr))
            instructions.append(char)
        curr = ""
    else:
        curr += char
if curr:
    instructions.append(int(curr))


class Node:
    def __init__(self):
        self.wall = None
        self.pos = None
        self.N = None
        self.E = None
        self.S = None
        self.W = None

    def neighbour(self, D):
        return {"N": self.N, "E": self.E, "S": self.S, "W": self.W}[D]


def findN(r, c):
    if r < 0:
        return findN(len(grid) - 1, c)
    if c >= len(grid[r]) or grid[r][c] == " ":
        return findN(r - 1, c)
    return (r, c)


def findE(r, c):
    if c >= len(grid[r]):
        return findE(r, 0)
    elif grid[r][c] == " ":
        return findE(r, c + 1)
    return (r, c)


def findS(r, c):
    if r >= len(grid):
        return findS(0, c)
    elif c >= len(grid[r]) or grid[r][c] == " ":
        return findS(r + 1, c)
    return (r, c)


def findW(r, c):
    if c < 0:
        return findW(r, len(grid[r]) - 1)
    elif grid[r][c] == " ":
        return findW(r, c - 1)
    return (r, c)


Nodes = defaultdict(Node)
foundMin = False
for r in range(len(grid)):
    for c in range(len(grid[r])):
        if grid[r][c] == " ":
            continue
        if not foundMin:
            START = Nodes[(r, c)]
            foundMin = True
        X = Nodes[(r, c)]
        X.wall = grid[r][c] == "#"
        X.pos = (r, c)
        X.N = Nodes[findN(r - 1, c)]
        X.E = Nodes[findE(r, c + 1)]
        X.S = Nodes[findS(r + 1, c)]
        X.W = Nodes[findW(r, c - 1)]


turnLeft = {"E": "N", "N": "W", "W": "S", "S": "E"}
turnRight = {"E": "S", "S": "W", "W": "N", "N": "E"}


D = "E"
X = START

for instr in instructions:
    if instr == "R":
        D = turnRight[D]
    elif instr == "L":
        D = turnLeft[D]
    else:
        steps = 0
        while steps < instr and not X.neighbour(D).wall:
            X = X.neighbour(D)
            # print(X.pos, D)
            steps += 1
    # print(X.pos, D)
facing = {"E": 0, "S": 1, "W": 2, "N": 3}
r, c = X.pos
print("P1", (r + 1) * 1000 + (c + 1) * 4 + facing[D])
