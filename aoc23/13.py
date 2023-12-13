import sys


def check_diff_V(m):
    wrong = []
    for dc in range(min(m, C - 2 - m) + 1):
        for r in range(R):
            if lines[r][m - dc] != lines[r][m + dc + 1]:
                wrong.append(((r, m - dc), (r, m + dc + 1)))
    return wrong


def check_diff_C(m):
    wrong = []
    for dr in range(min(m, R - 2 - m) + 1):
        for c in range(C):
            if lines[m - dr][c] != lines[m + dr + 1][c]:
                wrong.append(((m - dr, c), (m + dr + 1, c)))
    return wrong


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
            wrong = check_diff_V(m)
            if len(wrong) == P2:  # 0 for p1, 1 for p2
                s += m + 1
                break
        else:  # no point checking if break (have found)
            for m in range(R - 1):
                wrong = check_diff_C(m)
                if len(wrong) == P2:  # 0 for p1, 1 for p2
                    s += 100 * (m + 1)
                    break
    print(s)
