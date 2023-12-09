import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])

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

lines = lines.split("\n")
S = {}
As = []
for line in lines:
    a, b, c = remove(line).split()
    S[a] = (b, c)


s = 0
curr = "AAA"
while curr != "ZZZ":
    curr = S[curr][instr[s % N]]
    s += 1
print(s)

As = [x for x in S if x[-1] == "A"]
P2 = []
for curr in As:
    dist = 0
    while curr[-1] != "Z":
        curr = S[curr][instr[dist % N]]
        dist += 1
    P2.append(dist)

from math import lcm

print(lcm(*P2))
