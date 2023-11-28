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
S = list(enumerate(nums))
# (turn,num)
N = len(S)

for mix in range(10):
    for turn in range(N):
        for pos in range(N):
            if S[pos][0] == turn:
                num = S[pos][1]
                break

        if num % (N - 1) == 0:
            continue
        pop = S.pop(pos)

        S.insert((pos + num % (N - 1)) % N - 1, pop)

for pos in range(N):
    if S[pos][1] == 0:
        break
print("P2", S[(pos + 1000) % N][1] + S[(pos + 2000) % N][1] + S[(pos + 3000) % N][1])
