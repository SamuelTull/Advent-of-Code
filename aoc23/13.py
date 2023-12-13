import sys


data = "13.txt"
# data = "13test.txt"
if len(sys.argv) > 1:
    data = f"13{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

groups = data.split("\n\n")


for P2 in [False, True]:
    s = 0
    for group in groups:
        lines = group.split("\n")
        R = len(lines)
        C = len(lines[0])
        for m in range(C - 1):
            wrong = 0
            for dc in range(C):
                left = m - dc
                right = m + dc + 1
                if left < 0 or right >= C:
                    break
                for r in range(R):
                    if lines[r][left] != lines[r][right]:
                        wrong += 1
            if wrong == P2:  # 0 for p1, 1 for p2
                s += m + 1
                break
        else:  # no point checking if break (have found)
            for m in range(R - 1):
                wrong = 0
                for dr in range(R):
                    up = m - dr
                    down = m + dr + 1
                    if up < 0 or down >= R:
                        break
                    for c in range(C):
                        if lines[up][c] != lines[down][c]:
                            wrong += 1
                if wrong == P2:  # 0 for p1, 1 for p2
                    s += 100 * (m + 1)
                    break
    print(s)
