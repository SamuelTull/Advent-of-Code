import sys
from collections import defaultdict, deque
import heapq

DAY = 15
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
grid = [[int(x) for x in line.strip()] for line in data.split("\n")]

pos = (0, 0)

R = len(grid)
C = len(grid[0])


def get_h(pos):
    r, c = pos
    return 5 * R - 1 - r + 5 * C - 1 - c


def get_g(pos):
    r, c = pos
    shift = r // R + c // C
    val = grid[r % R][c % C]
    val += shift
    while val > 9:
        val -= 9
    return val


Q = []
heapq.heappush(Q, (0, 0, pos))
seen = set()

while Q:
    f, g, pos = heapq.heappop(Q)
    if pos == (5 * R - 1, 5 * C - 1):
        print(f)
        break
    if pos in seen:
        continue
    seen.add(pos)
    r, c = pos
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < 5 * R and 0 <= cc < 5 * C and (rr, cc) not in seen:
            new_g = g + get_g((rr, cc))
            new_h = get_h((rr, cc))
            new_f = new_g + new_h
            heapq.heappush(Q, (new_f, new_g, (rr, cc)))

# 3044 too high
