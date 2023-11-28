data = open("in.txt").read().strip()
# data = open("test.txt").read().strip()
lines = data.split("\n")
grid = [[l for l in line] for line in lines]
for g in grid:
    print(g)
# print(grid)
n = len(grid)
assert len(grid) == len(grid[0])  # square

visible = [[False for _ in l] for l in grid]
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            visible[i][j] = True
for i in range(1, n - 1):
    tall_A = grid[i][0]
    tall_B = grid[i][n - 1]
    tall_C = grid[0][i]
    tall_D = grid[n - 1][i]
    for j in range(1, n - 1):
        if grid[i][j] > tall_A:
            tall_A = grid[i][j]
            visible[i][j] = True
        if grid[i][n - 1 - j] > tall_B:
            tall_B = grid[i][n - 1 - j]
            visible[i][n - 1 - j] = True
        if grid[j][i] > tall_C:
            tall_C = grid[j][i]
            visible[j][i] = True
        if grid[n - 1 - j][i] > tall_D:
            tall_D = grid[n - 1 - j][i]
            visible[n - 1 - j][i] = True
print("P1", sum(sum(g for g in v) for v in visible))



def memoise(f):
    cache = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = f(*args, **kwargs)
        return cache[key]

    return wrapper


scenics = [[[0 for l in g] for g in grid] for i in range(4)]


@memoise
def scenic_number(i, j, direction):
    # direction = 0,1,2,3 = UP,DOWN,LEFT,RIGHT
    if i == 0 or j == 0 or i == n - 1 or j == n - 1:
        scenics[direction][i][j] = 0
        return 0
    shift = {0: [1, 0], 1: [-1, 0], 2: [0, 1], 3: [0, -1]}[direction]
    newi, newj = i + shift[0], j + shift[1]
    if grid[i][j] <= grid[newi][newj]:
        scenics[direction][i][j] = 0
        return 0
    else:
        s = 1 + scenic_number(newi, newj, direction)
        scenics[direction][i][j] = s
        return s