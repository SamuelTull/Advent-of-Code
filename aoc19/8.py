import sys
from collections import defaultdict, deque

DAY = 8
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()
data = [int(x) for x in data]

W = 25
H = 6

L = []
idx = 0
while idx < len(data):
    layer = []
    for _ in range(H):
        for _ in range(W):
            layer.append(data[idx])
            idx += 1
    L.append(layer)

"""minZ = 1e10
best = 0
for l in L:
    cnt0 = cnt1 = cnt2 = 0
    for x in l:
        if x == 0:
            cnt0 += 1
        elif x == 1:
            cnt1 += 1
        elif x == 2:
            cnt2 += 1
    if cnt0 < minZ:
        minZ = cnt0
        best = cnt1 * cnt2
print(best)"""

IMAG = []
for i in range(W * H):
    for layer in L:
        if layer[i] == 2:
            continue
        IMAG.append(layer[i])
        break
    else:
        assert False

for r in range(H):
    print("".join("#" if x == 1 else " " for x in IMAG[r * W : (r + 1) * W + 1]))
