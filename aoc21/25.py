import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

DAY = 25
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")


def print_grid():
    for r in range(R):
        for c in range(C):
            if (r, c) in E:
                print(">", end="")
            elif (r, c) in S:
                print("v", end="")
            else:
                print(".", end="")
        print()
    print()


R = len(lines)
C = len(lines[0])

E = set()
S = set()

for r in range(R):
    for c in range(C):
        if lines[r][c] == ">":
            E.add((r, c))
        elif lines[r][c] == "v":
            S.add((r, c))
# not checked
i = 0
while True:
    i += 1
    # print(i)
    # print_grid()
    E2 = set()
    for r, c in E:
        new = (r, (c + 1) % C)
        if not new in E and not new in S:
            E2.add(new)
        else:
            E2.add((r, c))
    S2 = set()
    for r, c in S:
        new = ((r + 1) % R, c)
        if not new in S and not new in E2:
            S2.add(new)
        else:
            S2.add((r, c))

    if E2 == E and S2 == S:
        print(i)
        break
    E = E2
    S = S2
