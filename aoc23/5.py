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
Q = deque([(curr[i], curr[i + 1]) for i in range(0, len(curr), 2)])

for group in groups:
    lines = group.split("\n")[1:]  # remove first line of text
    lines = sorted((list(map(int, line.split())) for line in lines), key=lambda x: x[1])
    source = [line[1] for line in lines]  # sorted list of all the bin starts
    Q1 = deque()
    while Q:
        c, dc = Q.pop()
        if c + dc < source[0]:  # c  fits entirely before bin
            next.append((c, dc))
            continue
        if c < source[0]:  # fits partially before bin
            Q1.append((c, source[0] - c))
            Q.append((source[0], dc - (source[0] - c)))
            continue
        i = bisect.bisect(source, c) - 1
        if i < len(source) - 1 and c + dc > source[i + 1]:
            # split into 2
            Q.append((source[i + 1], dc - (source[i + 1] - c)))
            dc = source[i + 1] - c
        bin_ends = source[i] + lines[i][2]
        if c + dc <= bin_ends:  # c < c + dc <= bin_ends -> add translated c
            Q1.append((lines[i][0] + c - source[i], dc))
        elif bin_ends <= c:  # bin_ends <= c < c + dc -> just add c
            Q1.append((c, dc))
        else:  # c < bin_ends < c + d -> split into two
            Q1.append((lines[i][0] + c - source[i], bin_ends - c))
            Q1.append((c + bin_ends - c, dc - (bin_ends - c)))
    Q = Q1
print(min(Q)[0])
