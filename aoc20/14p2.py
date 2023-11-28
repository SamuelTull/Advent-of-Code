import sys
from collections import defaultdict, deque

DAY = 14
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
M = {}
for line in lines:
    print(line)
    if line[:4] == "mask":
        mask = line.split(" ")[-1]
        continue
    line = line.replace("[", " ").replace("]", " ").split(" ")
    mem = list("".join("0" for _ in range(37)) + format(int(line[1]), "b"))[-36:]
    num = int(line[-1])
    for i, char in enumerate(mask):
        if char != "0":
            mem[i] = char

    Q = deque([mem])
    stillX = "X" in mem
    while stillX:
        if "X" in Q[0]:
            mem = Q.popleft()
            idx = mem.index("X")
            mem[idx] = "0"
            Q.append(mem.copy())
            mem[idx] = "1"
            Q.append(mem.copy())
        else:
            stillX = False

    for mem in Q:
        M[int("".join(mem), 2)] = num

print(sum(x for x in M.values()))
