import sys
from collections import defaultdict, deque

DAY = 4
PART = 2
# 12818 too low
data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n\n")
nums = [int(x) for x in lines[0].split(",")]
grids = [
    [[int(row[i : i + 2]) for i in range(0, len(row), 3)] for row in line.split("\n")]
    for line in lines[1:]
]


def solved(marked, i, j):
    if all(marked[i][jj] == 1 for jj in range(N)):
        return True
    if all(marked[ii][j] == 1 for ii in range(N)):
        return True
    return False


N = 5
best_num_i = 1e10


for grid_i, grid in enumerate(grids):
    cont = True
    marked = [[0 for _ in range(N)] for _ in range(N)]
    for num_i, num in enumerate(nums):
        if not cont:
            break
        for i in range(N):
            for j in range(N):
                if grid[i][j] == num:
                    marked[i][j] = 1
                    if solved(marked, i, j):
                        cont = False
                        if num_i < best_num_i:
                            best_num_i = num_i
                            best_sum = sum(
                                sum(grid[i][j] for i in range(N) if marked[i][j] == 0)
                                for j in range(N)
                            )
                            print("best", grid_i, num_i, num, best_num_i, best_sum)


print(best_sum * nums[best_num_i])
