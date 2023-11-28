import sys
from collections import defaultdict, deque, Counter

DAY = 14
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

line, pairings = data.split("\n\n")
line = line.strip()
pairs = {}
for pair in pairings.split("\n"):
    a, b = pair.split(" -> ")
    pairs[a] = b

for repeat in range(40):
    new_line = ""
    for i in range(len(line) - 1):
        if line[i : i + 2] in pairs:
            new_line += line[i] + pairs[line[i : i + 2]]
        else:
            new_line += line[i]
    new_line += line[-1]
    line = new_line

quantities = sorted(Counter(line).values())
print(quantities[-1] - quantities[0])
