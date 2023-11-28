import sys
from collections import defaultdict, deque
import ast

DAY = 18
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
lines = [ast.literal_eval(line) for line in lines]


def add(a, b):
    return reduce_([a, b])


def reduce_(a):
    a, didExplode = explode(a)
    if didExplode:
        return reduce_(a)
    a, didSplit = split(a)
    if didSplit:
        return reduce_(a)
    return a


def explode(a):
    return a


def split(a):
    if isinstance(a, int):
        if a >= 10:
            return [a // 2, (a + 1) // 2], True
        return a, False
    assert isinstance(a, list)
    a1, didSplit = split(a[0])
    if didSplit:
        return [a1, a[1]], True
    a2, didSplit = split(a[1])
    if didSplit:
        return [a[0], a2], True
    return a, False


P1 = lines[0]
for i in range(1, len(lines)):
    P1 = add(P1, lines[i])
