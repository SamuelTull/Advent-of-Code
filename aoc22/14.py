import sys
from collections import defaultdict
from utils import defaultlambdadict

data_dict = defaultlambdadict(
    lambda x: f"test{x}.txt",
    {
        "in": "in.txt",
        "0": "in.txt",
        0: "in.txt",
    },
)

try:
    data = data_dict[sys.argv[1]]
except:
    data = data_dict[0]


with open(data) as f:
    data = f.read().strip()
# print(data)
lines = data.split("\n")
lines = [
    [[int(x) for x in l.strip().split(",")] for l in line.split("->")] for line in lines
]
x1 = max(max(max(x[0] for x in line) for line in lines), 500) + 1
x0 = min(min(min(x[0] for x in line) for line in lines), 500) - 1
y1 = max(max(max(x[1] for x in line) for line in lines), 0) + 1
y0 = min(min(min(x[1] for x in line) for line in lines), 0)

r = x1 - x0
c = y1
print(r, c)
for i in range(len(lines)):
    for j in range(len(lines[i])):
        lines[i][j][0] -= x0
for l in lines:
    print(l)
grid = [[False for _ in range(r + 1)] for _ in range(c + 1)]

for line in lines:
    for i in range(1, len(line)):
        xi, yi = line[i - 1]
        xj, yj = line[i]
        # print(f"______{xi,yi} -> {xj,yj}")
        if xi == xj:
            yi, yj = sorted([yi, yj])
            for y in range(yi, yj + 1):
                # print(xi, y)
                grid[y][xi] = True

        elif yi == yj:
            xi, xj = sorted([xi, xj])
            for x in range(xi, xj + 1):
                # print(x, yi)
                grid[yi][x] = True

        else:
            print("DIAGONAL")


def print_grid():
    for g in grid:
        print("".join("#" if x else "." for x in g))


# if sand reaches x = 0 or max or y = max break

print_grid()

MAX_DEPTH = len(grid)
MAX_WIDTH = len(grid[0])
C = 0
end = False
while not end:
    s = (0, 500 - x0)
    moving = True
    while moving and not end:
        if not grid[s[0] + 1][s[1]]:
            s = (s[0] + 1, s[1])
        elif not grid[s[0] + 1][s[1] - 1]:
            s = (s[0] + 1, s[1] - 1)
        elif not grid[s[0] + 1][s[1] + 1]:
            s = (s[0] + 1, s[1] + 1)
        else:
            moving = False
        if s[0] == MAX_DEPTH - 1 or s[1] == 0 or s[1] == MAX_WIDTH - 1:
            end = True
    if not end:
        grid[s[0]][s[1]] = True
        C += 1
    # print_grid()


print(C)
