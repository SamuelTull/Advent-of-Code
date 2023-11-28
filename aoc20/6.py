import sys
from collections import defaultdict

DAY = 6
PART = 1, 2
data = str(DAY)
if len(sys.argv) > 1:
    if sys.argv[1] in ["0", "test"]:
        data = str(DAY) + "test"
    else:
        data = str(DAY) + sys.argv[1]

with open(data + ".txt") as f:
    data = f.read().strip()

groups = data.split("\n\n")
P1 = []
P2 = []
for group in groups:
    u = defaultdict(int)
    for i, line in enumerate(group.split("\n")):
        for char in line:
            u[char] += 1

    P2.append(len([x for x in u if u[x] == i + 1]))
    P1.append(len(u))

print(sum(P1))
print(sum(P2))
