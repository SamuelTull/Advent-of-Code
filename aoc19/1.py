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


def ans(x):
    y = x // 3 - 2
    if y < 0:
        return 0
    return y + ans(y)


lines = data.split("\n")
T = 0
for line in lines:
    T += ans(int(line))
print(T)
