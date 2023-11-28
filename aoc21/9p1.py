import sys
from collections import defaultdict, deque

DAY = 9
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
grid = [[int(x) for x in line.strip()] for line in data.split("\n")]
print(grid)

low_points = []
p1 = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        low = True
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[0]):
                if grid[i][j] >= grid[i + di][j + dj]:
                    low = False
                    break
        if low:
            low_points.append((i, j))
            p1 += 1 + grid[i][j]

print(p1)
