data = open("in.txt").read().strip()
# data = open("test.txt").read().strip()
lines = data.split("\n")
grid = [[int(l) for l in line] for line in lines]
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


scenics = [[[0 for l in g] for g in grid] for i in range(4)]

for direction in range(4):
    for i in range(0, n):
        for j in range(0, n):
            shiftI, shiftJ = {0: [-1, 0], 1: [0, -1], 2: [0, 1], 3: [1, 0]}[direction]
            newI = i
            newJ = j
            c = 0
            blocked = False
            while (
                (0 <= newI + shiftI <= n - 1 and 0 <= newJ + shiftJ <= n - 1)
                and not blocked
                and grid[i][j] >= grid[newI][newJ]
            ):
                c += 1
                newI += shiftI
                newJ += shiftJ
                if grid[newI][newJ] >= grid[i][j]:
                    blocked = True

            scenics[direction][i][j] = c


from math import prod

print(
    "P2",
    max(
        max(prod(scenics[direction][i][j] for direction in range(4)) for i in range(n))
        for j in range(n)
    ),
)


##########################################################
grid = [list(map(int, line)) for line in open(0).read().splitlines()]

t = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        k = grid[r][c]
        if (
            all(grid[r][x] < k for x in range(c))
            or all(grid[r][x] < k for x in range(c + 1, len(grid[r])))
            or all(grid[x][c] < k for x in range(r))
            or all(grid[x][c] < k for x in range(r + 1, len(grid)))
        ):
            t += 1

print(t)

t = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        k = grid[r][c]
        L = R = U = D = 0
        for x in range(c - 1, -1, -1):
            L += 1
            if grid[r][x] >= k:
                break
        for x in range(c + 1, len(grid[r])):
            R += 1
            if grid[r][x] >= k:
                break
        for x in range(r - 1, -1, -1):
            U += 1
            if grid[x][c] >= k:
                break
        for x in range(r + 1, len(grid)):
            D += 1
            if grid[x][c] >= k:
                break
        t = max(t, U * D * L * R)

print(t)
