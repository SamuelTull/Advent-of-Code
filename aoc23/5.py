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
    starts = [line[1] for line in lines]  # sorted list of all the bin starts
    ends = [line[1] + line[2] for line in lines]
    shifts = [line[0] - line[1] for line in lines]  # between start and end, shift
    Q_next = deque()
    while Q:
        c, dc = Q.popleft()
        if c + dc < starts[0]:  # c fits entirely before any bins
            Q_next.append((c, dc))
            continue
        if c < starts[0]:  # fits partially before bin
            Q_next.append((c, starts[0] - c))
            Q.appendleft((starts[0], dc - (starts[0] - c)))  # add rest back to queue
            continue
        i = bisect.bisect(starts, c) - 1  # c is to the right of starts[i]
        if i < len(starts) - 1 and c + dc > starts[i + 1]:
            # split into 2
            Q.appendleft((starts[i + 1], dc - (starts[i + 1] - c)))
            dc = starts[i + 1] - c
        if c + dc <= ends[i]:  # c < c + dc <= ends[i] -> add translated c
            Q_next.append((shifts[i] + c, dc))
        elif ends[i] <= c:  # ends[i] <= c < c + dc -> not translated
            Q_next.append((c, dc))
        else:  # c < ends[i] < c + d -> split into two
            Q_next.append((shifts[i] + c, ends[i] - c))
            Q_next.append((c + ends[i] - c, dc - (ends[i] - c)))
    Q = Q_next

print(min(Q)[0])
