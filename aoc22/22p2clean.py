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

#   |0|1|
#   |2|
# |4|3|
# |5|
N = 50
lines = data.split("\n\n")[0].split("\n")
G = []
G.append([[x for x in line[N : 2 * N]] for line in lines[:N]])
G.append([[x for x in line[2 * N :]] for line in lines[:N]])
G.append([[x for x in line[N : 2 * N]] for line in lines[N : 2 * N]])
G.append([[x for x in line[N : 2 * N]] for line in lines[2 * N : 3 * N]])
G.append([[x for x in line[:N]] for line in lines[2 * N : 3 * N]])
G.append([[x for x in line[:N]] for line in lines[3 * N :]])
N_ = 49


def step_old(g, r, c, d):
    if d == "N" and r - 1 >= 0:
        return (g, r - 1, c, d)
    if d == "S" and r + 1 < N:
        return (g, r + 1, c, d)
    if d == "E" and c + 1 < N:
        return (g, r, c + 1, d)
    if d == "W" and c - 1 >= 0:
        return (g, r, c - 1, d)
    return {
        (0, "N"): (5, c, 0, "E"),
        (0, "E"): (1, r, 0, d),
        (0, "S"): (2, 0, c, d),
        (0, "W"): (4, N - 1 - r, 0, "E"),
        (1, "N"): (5, N - 1, c, d),
        (1, "E"): (3, N - 1 - r, N - 1, "W"),
        (1, "S"): (2, c, N - 1, "W"),
        (1, "W"): (0, r, N - 1, d),
        (2, "N"): (0, N - 1, c, d),
        (2, "E"): (1, N - 1, r, "N"),
        (2, "S"): (3, 0, c, d),
        (2, "W"): (4, 0, r, "S"),
        (3, "N"): (2, N - 1, c, d),
        (3, "E"): (1, N - 1 - r, N - 1, "W"),
        (3, "S"): (5, c, N - 1, "W"),
        (3, "W"): (4, r, N - 1, d),
        (4, "N"): (2, c, 0, "E"),
        (4, "E"): (3, r, 0, d),
        (4, "S"): (5, 0, c, d),
        (4, "W"): (0, N - 1 - r, 0, "E"),
        (5, "N"): (4, N - 1, c, d),
        (5, "E"): (3, N - 1, r, "N"),
        (5, "S"): (1, 0, c, d),
        (5, "W"): (0, 0, r, "S"),
    }[g, d]


def step(g, r, c, d):
    match (g, r, c, d):
        case (0, 0, c, "N"):
            return (5, c, 0, "E")
        case (0, r, N_, "E"):
            return (1, r, 0, d)
        case (0, N_, c, "S"):
            return (2, 0, c, d)
        case (0, r, 0, "W"):
            return (4, N - 1 - r, 0, "E")
        case (1, 0, c, "N"):
            return (5, N - 1, c, d)
        case (1, r, N_, "E"):
            return (3, N - 1 - r, N - 1, "W")
        case (1, N_, c, "S"):
            return (2, c, N - 1, "W")
        case (1, r, 0, "W"):
            return (0, r, N - 1, d)
        case (2, 0, c, "N"):
            return (0, N - 1, c, d)
        case (2, r, N_, "E"):
            return (1, N - 1, r, "N")
        case (2, N_, c, "S"):
            return (3, 0, c, d)
        case (2, r, 0, "W"):
            return (4, 0, r, "S")
        case (3, 0, c, "N"):
            return (2, N - 1, c, d)
        case (3, r, N_, "E"):
            return (1, N - 1 - r, N - 1, "W")
        case (3, N_, c, "S"):
            return (5, c, N - 1, "W")
        case (3, r, 0, "W"):
            return (4, r, N - 1, d)
        case (4, 0, c, "N"):
            return (2, c, 0, "E")
        case (4, r, N_, "E"):
            return (3, r, 0, d)
        case (4, N_, c, "S"):
            return (5, 0, c, d)
        case (4, r, 0, "W"):
            return (0, N - 1 - r, 0, "E")
        case (5, 0, c, "N"):
            return (4, N - 1, c, d)
        case (5, r, N_, "E"):
            return (3, N - 1, r, "N")
        case (5, N_, c, "S"):
            return (1, 0, c, d)
        case (5, r, 0, "W"):
            return (0, 0, r, "S")
        case (g, r, c, "N"):
            return (g, r - 1, c, d)
        case (g, r, c, "S"):
            return (g, r + 1, c, d)
        case (g, r, c, "E"):
            return (g, r, c + 1, d)
        case (g, r, c, "W"):
            return (g, r, c - 1, d)
        case _:
            print("NO CASE!!!!!!!!")


turnLeft = {"E": "N", "N": "W", "W": "S", "S": "E"}
turnRight = {"E": "S", "S": "W", "W": "N", "N": "E"}

g, r, c, d = 0, 0, 0, "E"
for instr in data.split("\n\n")[1].replace("L", " L ").replace("R", " R ").split(" "):
    if instr == "R":
        d = turnRight[d]
    elif instr == "L":
        d = turnLeft[d]
    else:
        for steps in range(int(instr)):
            (g1, r1, c1, d1) = step_old(g, r, c, d)
            (g2, r2, c2, d2) = step(g, r, c, d)
            # assert (g1, r1, c1, d1) == (g2, r2, c2, d2), (
            #     (g, r, c, d),
            #     (g1, r1, c1, d1),
            #     (g2, r2, c2, d2),
            # )
            if G[g1][r1][c1] == "#":
                break
            g, r, c, d = g1, r1, c1, d1

assert g == 3
print("P2", (r + 101) * 1000 + (c + 51) * 4 + {"E": 0, "S": 1, "W": 2, "N": 3}[d])
