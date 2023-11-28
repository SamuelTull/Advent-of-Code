import sys
from collections import defaultdict, deque

DAY = 8
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
p1 = 0
for line in lines:
    data, target = line.split("|")
    data = data.split()
    target = target.split()
    for t in target:
        if len(t) in [2, 3, 4, 7]:
            p1 += 1
print(p1)
