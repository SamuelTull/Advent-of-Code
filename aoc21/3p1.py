import sys
from collections import defaultdict, deque

DAY = 3
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")

gamma = ""
beta = ""
for i in range(len(lines[0])):
    n_0 = 0
    n_1 = 0
    for line in lines:
        if line[i] == "0":
            n_0 += 1
        elif line[i] == "1":
            n_1 += 1
    if n_0 > n_1:
        gamma += "0"
        beta += "1"
    else:
        gamma += "1"
        beta += "0"


print(int(beta, 2) * int(gamma, 2))
