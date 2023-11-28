import sys
from collections import defaultdict, deque

DAY = 6
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()
lines = data.split("\n")


class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = set()


S = {}
for line in lines:
    x, y = line.split(")")
    if x in S:
        X = S[x]
    else:
        X = Node(x)
        S[x] = X

    if y in S:
        Y = S[y]
        X.children.add(Y)
        Y.parent = X

    else:
        Y = Node(y, X)
        X.children.add(Y)
        S[y] = Y
    if x == "COM":
        COM = X

total = 0
for X in S.values():
    while X.name != "COM":
        total += 1
        X = X.parent
print(total)


Q = deque([(S["YOU"].parent, 0)])
GOAL = S["SAN"].parent
SEEN = [S["YOU"].parent.name, "COM"]
T = 0
while Q:
    X, n = Q.popleft()
    if X == GOAL:
        print("P2", n)
    Y = X.parent
    if Y.name not in SEEN:  # add parent
        SEEN.append(Y.name)
        Q.append([Y, n + 1])
    for Y in X.children:  # add children
        if Y.name not in SEEN:
            SEEN.append(Y.name)
            Q.append([Y, n + 1])
print(T)
