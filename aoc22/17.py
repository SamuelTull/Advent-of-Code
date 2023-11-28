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
rocks = [
    [{(0, 0), (1, 0), (2, 0), (3, 0)}, (3, 0)],
    [{(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)}, (2, 2)],
    [{(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)}, (2, 2)],
    [{(0, 0), (0, 1), (0, 2), (0, 3)}, (0, 3)],
    [{(0, 0), (0, 1), (1, 0), (1, 1)}, (1, 1)],
]
# assuming 0,0 is bottom left:
# {position of blocks}, (width,height)

S = {(i, 0) for i in range(1, 8)}  # add the bottom of the pit
H = 0  # height
seen = {}  # states saved as (windID,rockID,{points relative to H})
i = 0
jumped = False
while i < 1000000000000:
    if i == 2022:
        print("P1", H)
    X, Y = (3, H + 5)
    rock, (rockR, rockT) = rocks[i % len(rocks)]
    moving = True
    while moving:
        Y -= 1
        wx = wind[windID]
        if not ((wx == -1 and X == 1) or (wx == 1 and X + rockR == 7)):
            blown = True
            for rx, ry in rock:
                if (X + wx + rx, Y + ry) in S:
                    blown = False
            if blown:
                X += wx
        for rx, ry in rock:
            if (X + rx, Y + ry - 1) in S:
                moving = False
        windID = (windID + 1) % len(wind)
    for rx, ry in rock:
        S.add((X + rx, Y + ry))
    H = max(H, Y + rockT)

    setID = (
        windID,
        i % len(rocks),
        frozenset((c, r - H) for (c, r) in S if r > H - 500),
    )
    if setID in seen and not jumped:
        prevI, prevH = seen[setID]
        dt = i - prevI
        if (1000000000000 - (i + 1)) % dt == 0:
            dh = H - prevH
            add = (1000000000000 - (i + 1)) // dt
            i += add * dt
            H += add * dh
            jumped = True
            break
    seen[setID] = (i, H)
    i += 1

print("P2", H)
