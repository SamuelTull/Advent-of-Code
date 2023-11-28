import sys
from collections import defaultdict

DAY = 9
PART = 1, 2

data = str(DAY)
P = 25
if False:  # change for test data debugging
    data = str(DAY) + "test"
    P = 5
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
    P = 5
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
lines = [int(x) for x in lines]

S = []
for i in range(len(lines)):
    if i >= P:
        valid = False
        for j in range(i - P, i):
            if valid:
                break
            for k in range(j + 1, i):
                a = S[k]
                b = S[j]
                c = lines[i]
                if S[k] + S[j] == lines[i]:
                    valid = True
                    break
        if not valid:
            GOAL = lines[i]
            print("P1", lines[i])
            break
    S.append(lines[i])


S = S[::-1]

start = 0
curr = 0
idx = 0

while True:
    curr += S[idx]
    if curr < GOAL:
        idx += 1
    elif curr > GOAL:
        start += 1
        idx = start
        curr = 0
    else:
        break
S = S[start : idx + 1]

x = min(S)
y = max(S)
print("P2", x + y)
