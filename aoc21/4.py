import sys
from collections import defaultdict, deque

DAY = 4
PART = 1
# 12818 too low
data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()


nums = None
grids = []
for line in data.split("\n\n"):
    if nums is None:
        nums = [int(x) for x in line.split(",")]
    else:
        rows = [[int(x) for x in row.split()] for row in line.split("\n")]
        grids.append(rows)


def solved(marked, i, j):
    if all(marked[i][jj] for jj in range(N)):
        return True
    if all(marked[ii][j] for ii in range(N)):
        return True
    return False


N = 5
worst_num_i = -1


for grid_i, grid in enumerate(grids):
    cont = True
    marked = [[False for _ in range(N)] for _ in range(N)]
    for num_i, num in enumerate(nums):
        if not cont:
            break
        for i in range(N):
            for j in range(N):
                if grid[i][j] == num:
                    marked[i][j] = True
                    if solved(marked, i, j):
                        cont = False
                        if num_i > worst_num_i:
                            worst_num_i = num_i
                            best_sum = sum(
                                sum(grid[i][j] for i in range(N) if not marked[i][j])
                                for j in range(N)
                            )
                            print("best", grid_i, num_i, num, worst_num_i, best_sum)


print(best_sum * nums[worst_num_i])
