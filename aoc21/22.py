import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

DAY = 22
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")

steps = []
X = set()
Y = set()
Z = set()

for line in lines:
    line = line.replace(",", " ").replace(".", " ").replace("=", " ")
    on, _, x1, x2, _, y1, y2, _, z1, z2 = line.split()
    x1, x2, y1, y2, z1, z2 = map(int, (x1, x2, y1, y2, z1, z2))
    X.add(x1)
    X.add(x2 + 1)
    Y.add(y1)
    Y.add(y2 + 1)
    Z.add(z1)
    Z.add(z2 + 1)
    steps.append([on == "on", x1, x2 + 1, y1, y2 + 1, z1, z2 + 1])

X = sorted(X)
Y = sorted(Y)
Z = sorted(Z)
Xn = len(X) - 1
Yn = len(Y) - 1
Zn = len(Z) - 1

G = set()
for i, (on, x1, x2, y1, y2, z1, z2) in enumerate(steps):
    # print(i, i / len(steps) * 100, len(G))
    i1 = X.index(x1)
    i2 = X.index(x2)
    j1 = Y.index(y1)
    j2 = Y.index(y2)
    k1 = Z.index(z1)
    k2 = Z.index(z2)
    for i in range(i1, i2):
        for j in range(j1, j2):
            for k in range(k1, k2):
                if on:
                    G.add((i, j, k))
                else:
                    G.discard((i, j, k))

S = 0
for n, (i, j, k) in enumerate(G):
    if n % 1000 == 0:
        print(n, n / len(G) * 100)
    S += (X[i + 1] - X[i]) * (Y[j + 1] - Y[j]) * (Z[k + 1] - Z[k])
print(S)
