import sys
from collections import defaultdict, deque

DAY = 1
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
lines = [int(x) for x in lines]

p2 = 0
for i in range(len(lines) - 3):
    if lines[i] < lines[i + 3]:
        p2 += 1

print(p2)
