with open("in.txt") as f:
    data = f.read().strip()
lines = data.split("\n")  # each line element of list
lines = [x.split(" ") for x in lines]


c = 1
x = 1
lst = []
for line in lines:
    if line[0] == "noop":
        if c % 40 == 20 % 40:
            lst.append(x * c)
        c += 1
    elif line[0] == "addx":
        for _ in range(2):
            if c % 40 == 20 % 40:
                lst.append(x * c)
            c += 1
        x += int(line[1])
    else:
        print("Unkown", line)

print("P1:", sum(lst))


def draw(row, col, grid, x):
    if col in (x - 1, x, x + 1):
        grid[row][col] = "#"


c = 0
x = 1
row = 0
col = 0


grid = [[" " for col in range(40)] for row in range(6)]
lst = []
for line in lines:
    if line[0] == "noop":
        draw(row, col, grid, x)
        c += 1
        row = c // 40
        col = c % 40
    elif line[0] == "addx":
        for _ in range(2):
            draw(row, col, grid, x)
            c += 1
            row = c // 40
            col = c % 40
        x += int(line[1])
    else:
        print("Unkown", line)

print("P2:")
for g in grid:
    print("".join(x for x in g))
