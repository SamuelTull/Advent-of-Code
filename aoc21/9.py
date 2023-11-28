import sys
from collections import defaultdict, deque

DAY = 9
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
R = len(grid)
C = len(grid[0])

low_points = []
p1 = 0
for r in range(R):
    assert len(grid[r]) == C
    for c in range(C):
        low = True
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (
                0 <= r + dr < R
                and 0 <= c + dc < C
                and grid[r][c] >= grid[r + dr][c + dc]
            ):
                low = False
                break
        if low:
            low_points.append((r, c))
            p1 += 1 + grid[r][c]

neighbours = []
for r, c in low_points:
    original = (r, c)
    seen = {(r, c)}
    q = deque([(r, c)])
    neighbours.append(0)
    while q:
        r, c = q.popleft()
        neighbours[-1] += 1
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if (
                0 <= r + dr < R
                and 0 <= c + dc < C
                and grid[r + dr][c + dc] < 9
                and (r + dr, c + dc) not in seen
            ):
                seen.add((r + dr, c + dc))
                q.append((r + dr, c + dc))

for i in range(len(low_points)):
    print(low_points[i], neighbours[i])

nines = []
for r in range(R):
    for c in range(C):
        if grid[r][c] == 9:
            nines.append((r, c))
assert len(nines) + sum(neighbours) == R * C

print(p1)
import math

print(sorted(neighbours)[:3], sorted(neighbours, reverse=True)[:3])
print(math.prod(sorted(neighbours, reverse=True)[:3]))
# 936000 too low
