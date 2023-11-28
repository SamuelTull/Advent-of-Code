import sys
from collections import defaultdict

DAY = 11
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()


def draw(occupied, empty):
    w = max(x[0] for x in occupied.union(empty))
    h = max(x[1] for x in occupied.union(empty))
    print()
    for y in range(h + 1):
        print(
            "".join(
                "#" if (x, y) in occupied else "L" if (x, y) in empty else "."
                for x in range(w + 1)
            )
        )
    print()


lines = data.split("\n")
empty = set()
occupied = set()
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x] == "L":
            empty.add((x, y))

changed = True
while changed:
    newempty = set()
    newoccupied = set()
    changed = False
    for x, y in empty:
        valid = True
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (x + dx, y + dy) in occupied:
                    valid = False
        if valid:
            newoccupied.add((x, y))
            changed = True
        else:
            newempty.add((x, y))

    for x, y in occupied:
        c = -1
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if (x + dx, y + dy) in occupied:
                    c += 1
        if c < 4:
            newoccupied.add((x, y))
        else:
            newempty.add((x, y))
            changed = True
    occupied = newoccupied
    empty = newempty
    # draw(occupied, empty)


print("P1", len(occupied))
