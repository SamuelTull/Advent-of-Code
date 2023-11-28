import sys
from collections import defaultdict, deque

DAY = 20
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

code, image = data.split("\n\n")
image = image.split("\n")
G = set()
for r in range(len(image)):
    for c in range(len(image[r])):
        if image[r][c] == "#":
            G.add((r, c))


def get_neighbors(pt):
    r, c = pt
    return [
        (r - 1, c - 1),
        (r - 1, c),
        (r - 1, c + 1),
        (r, c - 1),
        (r, c),
        (r, c + 1),
        (r + 1, c - 1),
        (r + 1, c),
        (r + 1, c + 1),
    ]


# ...
# ...
# ... -> #

# ###
# ###
# ### -> .

# so alternate between recording #s and .s.


def get_r_c(G):
    min_r = min([x[0] for x in G]) - 1
    max_r = max([x[0] for x in G]) + 1
    min_c = min([x[1] for x in G]) - 1
    max_c = max([x[1] for x in G]) + 1
    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            yield r, c


for repeat in range(25):
    G1 = set()
    for r, c in get_r_c(G):
        s = 0
        for i, pt in enumerate(get_neighbors((r, c))[::-1]):
            s += 1 << i if pt in G else 0
        if code[s] == ".":
            G1.add((r, c))

    G2 = set()
    for r, c in get_r_c(G1):
        s = 0
        for i, pt in enumerate(get_neighbors((r, c))[::-1]):
            s += 1 << i if pt not in G1 else 0
        if code[s] == "#":
            G2.add((r, c))
    if repeat == 0:
        print("P1", len(G2))
    G = G2
print("P2", len(G2))
