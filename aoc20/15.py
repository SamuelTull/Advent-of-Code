import sys
from collections import defaultdict

DAY = 15
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

start = [int(x) for x in data.split(",")]
N = len(start)

S = {}
i = 1
for s in start:
    S[s] = (i, None)
    i += 1
    prev = s

for i in range(i, 30000000 + 1):
    if S[prev][1] == None:
        S[0] = (i, S[0][0])
        prev = 0
    else:
        new = S[prev][0] - S[prev][1]
        if new in S:
            S[new] = (i, S[new][0])
        else:
            S[new] = (i, None)
        prev = new

print(prev)
