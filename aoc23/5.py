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
curr = list(map(int, groups.pop(0).split()[1:]))  # pop seeds from groups
Q = deque([(curr[i], curr[i] + curr[i + 1] - 1) for i in range(0, len(curr), 2)])


for group in groups:
    lines = group.split("\n")[1:]  # remove first line of text
    lines = sorted((list(map(int, line.split())) for line in lines), key=lambda x: x[1])
    starts = [line[1] for line in lines]  # sorted list of all the bin starts
    ends = [line[1] + line[2] for line in lines]
    # if a point is between start and end, it is shifted by line[0] - line[1]
    shifts = [line[0] - line[1] for line in lines]
    Q_next = deque()
    while Q:
        st, ed = Q.pop()  # start, end
        if ed < starts[0]:  # fits entirely before any bins
            Q_next.append((st, ed))  # unshifted
            continue
        if st < starts[0]:  # fits partially before bin
            # split into [st,starts[0]-1] and [starts[0],ed]
            Q_next.append((st, starts[0] - 1))  # first split unshifted
            st, ed = starts[0], ed  # second split
        i = bisect.bisect(starts, st) - 1  # starts[i] <= st < starts[i+1]
        if i < len(starts) - 1 and ed > starts[i + 1]:  # st < starts[i + 1] < ed
            # split into [st,starts[i + 1]-1] and [starts[i + 1],ed]
            Q.append((starts[i + 1], ed))  # 2nd split later (may overlap more)
            ed = starts[i + 1] - 1  # first split now
        if ed <= ends[i]:  # st < ed <= ends[i]
            Q_next.append((shifts[i] + st, shifts[i] + ed))  # all shifted
        elif ends[i] <= st:  # ends[i] <= st < ed
            Q_next.append((st, ed))  # all unshifted
        else:  # st < ends[i] < ed
            # split into [st,end[i] -1 ] and [ends[i],ed]
            Q_next.append((shifts[i] + st, shifts[i] + ends[i] - 1))  # split 1 shifted
            Q_next.append((ends[i], ed))  # split 2 unshifted
    Q = Q_next
print(min(Q)[0])
