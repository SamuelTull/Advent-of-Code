import sys
from collections import defaultdict, deque

DAY = 22
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read()
grid, instructions = data.split("\n\n")

N = 50
g1 = [[x for x in line[N : 2 * N]] for line in grid.split("\n")[:N]]
g2 = [[x for x in line[2 * N :]] for line in grid.split("\n")[:N]]
g3 = [[x for x in line[N : 2 * N]] for line in grid.split("\n")[N : 2 * N]]
g4 = [[x for x in line[N : 2 * N]] for line in grid.split("\n")[2 * N : 3 * N]]
g5 = [[x for x in line[:N]] for line in grid.split("\n")[2 * N : 3 * N]]
g6 = [[x for x in line[:N]] for line in grid.split("\n")[3 * N :]]
grids = {1: g1, 2: g2, 3: g3, 4: g4, 5: g5, 6: g6}

instructions = instructions.replace("L", " L ").replace("R", " R ").split(" ")


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


def findN(g, r, c):
    if r - 1 >= 0:
        return g, r - 1, c
    # else have fallen off
    return {
        1: (6, c, 0),
        2: (6, N - 1, c),
        3: (1, N - 1, c),
        4: (3, N - 1, c),
        5: (3, c, 0),
        6: (5, N - 1, c),
    }[g]


def findS(g, r, c):
    if r + 1 < N:
        return g, r + 1, c
    return {
        1: (3, 0, c),
        2: (3, c, N - 1),
        3: (4, 0, c),
        4: (6, c, N - 1),
        5: (6, 0, c),
        6: (2, 0, c),
    }[g]


def findE(g, r, c):
    if c + 1 < N:
        return g, r, c + 1
    return {
        1: (2, r, 0),
        2: (4, N - 1 - r, N - 1),
        3: (2, N - 1, r),
        4: (2, N - 1 - r, N - 1),
        5: (4, r, 0),
        6: (4, N - 1, r),
    }[g]


def findW(g, r, c):
    if c - 1 >= 0:
        return g, r, c - 1
    return {
        1: (5, N - 1 - r, 0),
        2: (1, r, N - 1),
        3: (5, 0, r),
        4: (5, r, N - 1),
        5: (1, N - 1 - r, 0),
        6: (1, 0, r),
    }[g]


Nodes = defaultdict(Node)
foundMin = False
for g in range(1, 7):
    for r in range(N):
        for c in range(N):
            if (g, r, c) == (4, 0, 0):
                pass

            X = Nodes[(g, r, c)]
            X.wall = grids[g][r][c] == "#"
            X.pos = (g, r, c)
            X.N = Nodes[findN(g, r, c)]
            X.E = Nodes[findE(g, r, c)]
            X.S = Nodes[findS(g, r, c)]
            X.W = Nodes[findW(g, r, c)]


turnLeft = {"E": "N", "N": "W", "W": "S", "S": "E"}
turnRight = {"E": "S", "S": "W", "W": "N", "N": "E"}
correctD = {
    (1, 6): "E",
    (1, 5): "E",
    (2, 4): "W",
    (2, 3): "W",
    (3, 2): "N",
    (3, 5): "S",
    (4, 2): "W",
    (4, 6): "W",
    (5, 1): "E",
    (5, 3): "E",
    (6, 1): "S",
    (6, 4): "N",
}

X, D = Nodes[(1, 0, 0)], "E"
for instr in instructions:
    if instr == "R":
        D = turnRight[D]
    elif instr == "L":
        D = turnLeft[D]
    else:
        instr = int(instr)
        steps = 0
        while steps < instr and not X.neighbour(D).wall:
            oldX = X
            gOld = X.pos[0]
            X = X.neighbour(D)
            gNew = X.pos[0]
            if (gOld, gNew) in correctD:
                D = correctD[(gOld, gNew)]
            steps += 1

g, r, c = X.pos
assert g == 4
print("P2", (r + 101) * 1000 + (c + 51) * 4 + {"E": 0, "S": 1, "W": 2, "N": 3}[D])


def debug(g, r, c, D):
    print("Debug", (g, r, c), D, end=": ")
    START = X = Nodes[(g, r, c)]
    for i in range(4 * N):
        gOld = X.pos[0]
        X = X.neighbour(D)
        gNew = X.pos[0]
        if (gOld, gNew) in correctD:
            D = correctD[(gOld, gNew)]
    if X == START:
        print("Passed")
    else:
        print("Failed")


debug(1, 1, 1, "N")
