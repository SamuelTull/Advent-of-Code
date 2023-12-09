import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

data = "8.txt"
# data = "8test.txt"
if len(sys.argv) > 1:
    data = f"8{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

instr, lines = data.split("\n\n")
instr = instr.replace("L", "0").replace("R", "1")
instr = [int(x) for x in instr]
N = len(instr)


S = {}
lines = lines.split("\n")
As = []
Zs = []
for line in lines:
    a, b, c = (
        line.replace("=", "").replace("(", "").replace(")", "").replace(",", "").split()
    )
    S[a] = (b, c)
    if a[-1] == "A":
        As.append(a)
    elif a[-1] == "Z":
        Zs.append(a)

states_start = set()
for a in As:
    curr = a
    dist = 0
    while curr[-1] != "Z":
        curr = S[curr][instr[dist % N]]
        dist += 1
    states_start.add((curr, dist, dist % N))


states = {}
for i in range(N):
    for z in Zs:
        curr = S[z][instr[i]]
        dist = 1
        SEEN = {(curr, (dist + i) % N)}
        while curr[-1] != "Z":
            curr = S[curr][instr[(dist + i) % N]]
            dist += 1
            if (curr, (dist + i) % N) in SEEN:
                break
            SEEN.add((curr, (dist + i) % N))
        else:
            states[(z, i)] = (curr, dist)

print(states_start)
print("=============")
for s in sorted(states):
    print(s, states[s], states_start)


assert False
print("LEN", len(states))
min_dist = -1
Q = deque(states_start)
while Q:
    print(Q)
    curr, dist = Q.popleft()
    # print(curr, S[curr], dist)
    if dist == min_dist:
        break
    while dist < min_dist:
        curr, ddist = states[(curr, dist % N)]
        dist += ddist
    Q.append((curr, dist))
    min_dist = max(min_dist, dist)
print(min_dist)
