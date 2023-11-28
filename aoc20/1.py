import sys
from collections import defaultdict

DAY = 1
data = str(DAY) + ".txt"
if len(sys.argv) > 1:
    if sys.argv[1] in ["0", "test"]:
        data = str(DAY) + "test.txt"
    else:
        data = str(DAY) + sys.argv[1] + ".txt"

with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")
lines = [int(x) for x in lines]
for i in range(len(lines)):
    for j in range(i, len(lines)):
        for k in range(j, len(lines)):
            if lines[i] + lines[j] + lines[k] == 2020:
                print("P1", lines[i] * lines[j] * lines[k])
