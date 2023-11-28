import sys
from collections import defaultdict, deque


DAY = 20
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
nums = [int(x) * 811589153 for x in lines]
S = {}
for i, num in enumerate(nums):
    S[i] = (i, num)
N = len(S)

for mix in range(10):
    for idx in range(N):
        pos, num = [(pos, num) for pos, (i, num) in S.items() if i == idx][0]

        if num % (N - 1) == 0:
            continue

        for i in range(pos, pos + num % (N - 1)):
            S[(i) % N] = S[(i + 1) % N]
        S[(i + 1) % N] = (idx, num)

pos = [pos for pos, (_, num) in S.items() if num == 0][0]
print("P2", S[(pos + 1000) % N][1] + S[(pos + 2000) % N][1] + S[(pos + 3000) % N][1])
