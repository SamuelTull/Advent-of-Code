import sys
from collections import defaultdict, deque

DAY = 2
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
lines = [x.split(" ") for x in lines]

X = 0
Y = 0

for line in lines:
    if line[0] == "up":
        Y -= int(line[1])
    elif line[0] == "down":
        Y += int(line[1])
    elif line[0] == "forward":
        X += int(line[1])
print(X * Y)
