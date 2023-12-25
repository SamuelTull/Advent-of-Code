import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])


data = "24.txt"
# data = "24test.txt"
if len(sys.argv) > 1:
    data = f"24{sys.argv[1]}.txt"
with open(data) as f:
    if data == "24test.txt":
        ym, yM = 7, 27
        xm, xM = 7, 27
    else:
        ym, yM = 200000000000000, 400000000000000
        xm, xM = 200000000000000, 400000000000000
    data = f.read().strip()

lines = data.split("\n")
for i, line in enumerate(lines):
    line = remove(line, "@,").split()
    lines[i] = [int(x) for x in line]
N = len(lines)


s = 0
for i in range(N):
    for j in range(i + 1, N):
        x1, y1, _, dx1, dy1, _ = lines[i]
        x2, y2, _, dx2, dy2, _ = lines[j]

        m1 = dy1 / dx1
        m2 = dy2 / dx2
        c1 = y1 - m1 * x1
        c2 = y2 - m2 * x2

        if m1 == m2:
            assert c1 != c2, "same line"
            continue  # paralell lines

        xi = (c2 - c1) / (m1 - m2)
        yi = m1 * xi + c1

        t1 = (xi - x1) / dx1
        t2 = (xi - x2) / dx2

        if (xm <= xi <= xM) and (ym <= yi <= yM) and t1 > 0 and t2 > 0:
            s += 1

print(s)
