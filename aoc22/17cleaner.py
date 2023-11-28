import sys
from collections import defaultdict, deque

DAY = 17
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

wind = [1 if char == ">" else -1 for char in data]
windID = 0


def rocks(i, X, Y):
    if i == 0:
        return {(X, Y), (1 + X, Y), (2 + X, Y), (3 + X, Y)}
    if i == 1:
        return {
            (1 + X, Y),
            (X, 1 + X),
            (1 + X, 1 + Y),
            (2 + X, 1 + Y),
            (1 + X, 2 + Y),
        }
    if i == 2:
        return {(X, Y), (1 + X, Y), (2 + X, Y), (2 + X, 1 + Y), (2 + X, 2 + Y)}
    if i == 3:
        return {(X, Y), (X, 1 + Y), (X, 2 + Y), (X, 3 + Y)}
    if i == 4:
        return {(X, Y), (X, 1 + Y), (1 + X, Y), (1 + X, 1 + Y)}


def rockDim(i):
    return [(3, 0), (2, 2), (2, 2), (0, 3), (1, 1)][i]


# assuming 0,0 is bottom left:
# {position of blocks}, (width,height)

S = {(i, 0) for i in range(1, 8)}  # add the bottom of the pit
H = 0  # height
seen = {}  # states saved as (windID,rockID,{points relative to H})
i = 0
jumped = False
while i < 1000000000000:
    X, Y = (3, H + 5)
    rockW, rockH = rockDim(i % 5)
    moving = True
    while moving:
        Y -= 1
        wx = wind[windID]
        if not ((wx == -1 and X == 1) or (wx == 1 and X + rockW == 7)):
            if not rocks(i % 5, X + wx, Y) & S:
                X += wx
        if rocks(i % 5, X, Y - 1) & S:
            moving = False
        windID = (windID + 1) % len(wind)

    S |= rocks(i % 5, X, Y)
    H = max(H, Y + rockH)

    setID = (
        windID,
        i % 5,
        frozenset((c, r - H) for (c, r) in S if r > H - 500),
    )
    if setID in seen and not jumped:
        prevI, prevH = seen[setID]
        dt = i - prevI
        dh = H - prevH
        add = (1000000000000 - i) // dt
        i += add * dt
        jumped = True
    seen[setID] = (i, H)
    i += 1
print(i, H + add * dh, len(S))
