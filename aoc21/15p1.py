import sys
from collections import defaultdict, deque
import heapq

DAY = 15
PART = 1

data = str(DAY)
if True:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
grid = [[int(x) for x in line.strip()] for line in data.split("\n")]

pos = (0, 0)

# A* search
R = len(grid)
C = len(grid[0])


def get_h(pos):
    r, c = pos
    return R - 1 - r + C - 1 - c


Q = []
heapq.heappush(Q, (0, 0, pos))
seen = set()
seen.add(pos)

while Q:
    f, g, pos = heapq.heappop(Q)
    seen.add(pos)
    if pos == (R - 1, C - 1):
        print(f)
        break
    r, c = pos
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < R and 0 <= cc < C and (rr, cc) not in seen:
            new_g = g + grid[rr][cc]
            new_h = get_h((rr, cc))
            new_f = new_g + new_h
            heapq.heappush(Q, (new_f, new_g, (rr, cc)))
            seen.add((rr, cc))
