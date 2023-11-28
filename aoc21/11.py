import sys
from collections import defaultdict, deque

DAY = 11
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()


def print_grid(grid):
    for row in grid:
        print("".join(str(x) for x in row))
    print()


lines = data.split("\n")
grid = [[int(x) for x in line.strip()] for line in data.split("\n")]
R = C = 10
p1 = 0
step = 0
while not all(all(x == 0 for x in row) for row in grid):
    grid = [[grid[r][c] + 1 for c in range(C)] for r in range(R)]
    finished = False
    while not finished:
        finished = True
        for r in range(R):
            for c in range(C):
                if grid[r][c] > 9:
                    if step < 100:
                        p1 += 1
                    finished = False
                    grid[r][c] = 0
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            rr = r + dr
                            cc = c + dc
                            if 0 <= rr < R and 0 <= cc < C and grid[rr][cc]:
                                # equal to zero == flashed already
                                grid[rr][cc] += 1

    step += 1

print(p1)
print(step)
