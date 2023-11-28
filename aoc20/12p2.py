import sys
from collections import defaultdict

DAY = 12
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()


def sign(x):
    return 1 if x >= 0 else -1


def rotate_90(d, wx, wy):
    assert d in ["R", "L"]
    if d == "R":
        sx, sy = {
            (-1, -1): (1, -1),
            (1, -1): (1, 1),
            (1, 1): (-1, 1),
            (-1, 1): (-1, -1),
        }[sign(wx), sign(wy)]

    else:
        sx, sy = {
            (1, -1): (-1, -1),
            (1, 1): (1, -1),
            (-1, 1): (1, 1),
            (-1, -1): (-1, 1),
        }[sign(wx), sign(wy)]

    return (sx * abs(wy), sy * abs(wx))


lines = data.split("\n")
x = y = 0
wx, wy = (10, -1)
heading = "E"
turnLeft = {"E": "N", "N": "W", "W": "S", "S": "E"}
turnRight = {"E": "S", "S": "W", "W": "N", "N": "E"}
D = {"E": (1, 0), "N": (0, -1), "W": (-1, 0), "S": (0, 1)}

for line in lines:
    ins = line[0]
    val = int(line[1:])

    if ins == "R":
        if val == 180:
            wx = -wx
            wy = -wy
        elif val == 90:
            wx, wy = rotate_90("R", wx, wy)
        elif val == 270:
            wx, wy = rotate_90("L", wx, wy)

    elif ins == "L":
        if val == 180:
            wx = -wx
            wy = -wy
        elif val == 270:
            wx, wy = rotate_90("R", wx, wy)
        elif val == 90:
            wx, wy = rotate_90("L", wx, wy)

    elif ins == "F":
        x += val * wx
        y += val * wy
    else:
        dx, dy = D[ins]
        wx += val * dx
        wy += val * dy


print(abs(x) + abs(y))
