import sys
from collections import defaultdict

DAY = 13
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

_, info = data.split("\n")

idx = []
bus = []
missedBy = []
B = []


# t = 0 mod(B[0])
# t + i = 0 mod(B[i])
# t = -i mod(B[i])
for i, b in enumerate(info.split(",")):
    if b != "x":
        B.append((-i % int(b), int(b)))

num = len(B)
for i in range(num):
    for j in range(i + 1, num):
        if B[i][1] % B[j][1] == 0 or B[j][1] % B[i][1] == 0:
            assert False, f"Not Pairwise Coprime {B[i][1]},{B[j][1]}"

B.sort(reverse=True, key=lambda x: x[1])

X = B[0][0]
cong = B[0][1]
for i in range(1, len(B)):
    (ai, ni) = B[i]
    while X % ni != ai:
        X += cong
    cong *= ni
print(X)
