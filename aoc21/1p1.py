import sys
from collections import defaultdict, deque

DAY = 1
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
lines = [int(x) for x in lines]
p1 = 0
for i in range(len(lines) - 1):
    if lines[i] < lines[i + 1]:
        p1 += 1

print(p1)
