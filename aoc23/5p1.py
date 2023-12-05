import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)
import bisect

data = "5.txt"
# data = "5test.txt"
if len(sys.argv) > 1:
    data = f"5{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

groups = data.split("\n\n")
curr = list(map(int, groups.pop(0).split()[1:]))

for group in groups:
    next = []
    lines = group.split("\n")[1:]
    lines = sorted((list(map(int, line.split())) for line in lines), key=lambda x: x[1])
    starts = [lines[1] for lines in lines]
    for c in curr:
        if c < starts[0]:
            next.append(c)
            continue
        i = bisect.bisect_right(starts, c) - 1
        # check if within range
        dc = c - starts[i]
        if dc < lines[i][2]:
            next.append(lines[i][0] + dc)
        else:
            next.append(c)
    curr = next
print(min(curr))
