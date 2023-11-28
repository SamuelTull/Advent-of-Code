import sys
from collections import defaultdict, deque

DAY = 11
PART = 2

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
for step in range(100):
    print(p1)
    print_grid(grid)
    flashed = [[False for _ in range(C)] for _ in range(R)]
    new_grid = [[grid[r][c] + 1 for c in range(C)] for r in range(R)]
    finished = False
    while not finished:
        finished = True
        for r in range(R):
            for c in range(C):
                if not flashed[r][c] and new_grid[r][c] > 9:
                    finished = False
                    flashed[r][c] = True
                    new_grid[r][c] = 0
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            if (
                                0 <= r + dr < R
                                and 0 <= c + dc < C
                                and not flashed[r + dr][c + dc]
                            ):
                                new_grid[r + dr][c + dc] += 1

    p1 += sum(sum(row) for row in flashed)
    grid = new_grid

print(p1)
