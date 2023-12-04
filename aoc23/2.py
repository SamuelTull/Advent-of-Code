import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

data = "2.txt"
# data = "2test.txt"
if len(sys.argv) > 1:
    data = f"2{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()
lines = data.split("\n")

s = 0
s2 = 0
for i, line in enumerate(lines):
    turns = line.replace(":", ";").split("; ")[1:]
    possible = True
    p2 = defaultdict(int)
    for turn in turns:
        cols = defaultdict(int)
        for pick in turn.split(", "):
            num, col = pick.split()
            cols[col] += int(num)
            p2[col] = max(p2[col], int(num))
        if cols["red"] > 12 or cols["green"] > 13 or cols["blue"] > 14:
            possible = False
    s += possible * (i + 1)
    s2 += p2["red"] * p2["green"] * p2["blue"]


print(s)
print(s2)
