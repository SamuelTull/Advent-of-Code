import sys
from collections import defaultdict, deque

DAY = 17
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

wind = [1 if char == ">" else -1 if char == "<" else None for char in data]
windLen = len(wind)
windID = 0
assert None not in wind

rocks = [
    {0, 1, 2, 3},
    {1, 1j, 1 + 1j, 2 + 1j, 1 + 2j},
    {0, 1, 2, 2 + 1j, 2 + 2j},
    {0, 1j, 2j, 3j},
    {0, 1j, 1, 1 + 1j},
]
rockLen = len(rocks)
H = 0
S = set()


for i in range(2022):
    X = 3 + (H + 5) * 1j
    rock = rocks[i % rockLen]
    moving = True
    while moving:
        X -= 1j
        dx = wind[windID % windLen]
        blown = True
        for dr in rock:
            this = X + dr + dx
            if X + dr + dx in S or (X + dr + dx).real in [0, 8]:
                blown = False
                break
        if blown:
            X += dx
        for dr in rock:
            this = X + dr - 1j
            if X + dr - 1j in S or (X + dr - 1j).imag <= 0:
                moving = False
        windID += 1

    to_add = {X + dr for dr in rock}
    S |= {X + dr for dr in rock}
    newH = max((X + dr).imag for dr in rock)
    H = max(H, int(max((X + dr).imag for dr in rock)))
print(H)
