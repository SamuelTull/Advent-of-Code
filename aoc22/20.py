import sys
from collections import defaultdict, deque

DAY = 20
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
nums = [int(x) for x in lines]
S = {}
for i, num in enumerate(nums):
    S[i] = (i, num)
N = len(S)

del nums, lines, f, data
# while True:
for idx in range(N):
    pos, num = [(pos, num) for pos, (i, num) in S.items() if i == idx][0]
    # print([x[1] for x in S.values()])
    print(idx, int(idx / N * 100))
    oldnum = num
    if num > 0 and pos + num >= N - 1:
        num = -N + num + 1

    elif num < 0 and pos + num <= 0:
        num = N + num - 1

    if num > 0:
        for i in range(pos, pos + num):
            S[(i) % N] = S[(i + 1) % N]
        S[(i + 1) % N] = (idx, oldnum)

    elif num < 0:
        for i in range(pos, pos + num, -1):
            S[(i) % N] = S[(i - 1) % N]
        S[(i - 1) % N] = (idx, oldnum)

pos = [pos for pos, (_, num) in S.items() if num == 0][0]
# print(S[(pos + 1000) % N][1], S[(pos + 2000) % N][1], S[(pos + 3000) % N][1])
print("P1", S[(pos + 1000) % N][1] + S[(pos + 2000) % N][1] + S[(pos + 3000) % N][1])
