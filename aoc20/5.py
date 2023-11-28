import sys
from collections import defaultdict

DAY = 5
PART = 1
data = str(DAY)
if len(sys.argv) > 1:
    if sys.argv[1] in ["0", "test"]:
        data = str(DAY) + "test"
    else:
        data = str(DAY) + sys.argv[1]

with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
rows = 128
seats = 8
S = set()
# groups = data.split("\n\n")
# grid = [[x for x in line.strip()] for line in data.split("\n")]
# lines = [int(x) for x in lines]
# lines = [x.replace("-", ",").split(",") for x in lines]
# lines = [x.split(" ") for x in lines]

for line in lines:
    X = line[:7].replace("F", "0").replace("B", "1")
    Y = line[7:].replace("L", "0").replace("R", "1")
    row = int(X, 2)
    seat = int(Y, 2)
    S.add((row, seat))
s = max(S)
print("P1", s[0] * 8 + s[1])

ids = []
for s in S:
    ids.append(s[0] * 8 + s[1])
ids.sort()


for i in range(len(ids) - 1):
    if ids[i - 1] == ids[i] - 2:
        print("P2", ids[i] - 1)
