import sys
from collections import defaultdict, deque

DAY = 20
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

code, image = data.split("\n\n")
image = [[x for x in line.strip()] for line in image.split("\n")]
G = set()
for r in range(len(image)):
    for c in range(len(image[r])):
        if image[r][c] == "#":
            G.add((r, c))


# 3x3 0s is 1 so only record 0s for step 1
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


min_r = min([x[0] for x in G]) - 1
max_r = max([x[0] for x in G]) + 1
min_c = min([x[1] for x in G]) - 1
max_c = max([x[1] for x in G]) + 1
G1 = set()
for r in range(min_r, max_r + 1):
    for c in range(min_c, max_c + 1):
        s = 0
        for i, pt in enumerate(get_neighbors((r, c))[::-1]):
            s += 1 << i if pt in G else 0
        if code[s] == ".":
            G1.add((r, c))

map = [[1 for _ in range(max_c - min_c + 1)] for _ in range(max_r - min_r + 1)]
for r, c in G1:
    map[r - min_r][c - min_c] = 0


min_r = min([x[0] for x in G1]) - 1
max_r = max([x[0] for x in G1]) + 1
min_c = min([x[1] for x in G1]) - 1
max_c = max([x[1] for x in G1]) + 1
G2 = set()
for r in range(min_r, max_r + 1):
    for c in range(min_c, max_c + 1):
        s = 0
        for i, pt in enumerate(get_neighbors((r, c))[::-1]):
            s += 1 << i if pt not in G1 else 0
        if code[s] == "#":
            G2.add((r, c))

print(len(G2))

# 102 too low
# 9506 too high
# 9704 TOO HIGHT
# 10013?
