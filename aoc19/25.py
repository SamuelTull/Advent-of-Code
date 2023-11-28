import sys
from collections import defaultdict, deque

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


def transform(val, sub):
    return (val * sub) % 20201227


val = 1
for step in range(12):
    print(step, val)
    val = transform(val, 7)
