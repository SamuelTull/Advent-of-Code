import sys
from collections import deque

data = "21.txt"
# data = "21test.txt"
if len(sys.argv) > 1:
    data = f"21{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")

G = set()
R = len(lines)
C = len(lines[0])

assert R == C
for r, row in enumerate(lines):
    for c, x in enumerate(row):
        if x == "#":
            G.add((r, c))
        elif x == "S":
            S = (r, c)


Q = deque([(*S, 0)])
SEEN = {S}
odd = 0
even = 0
curr = 0

P1 = 64

A1 = A2 = A3 = A4 = -1
P2 = 26501365


def analytic(n):
    # spotted the 2nd difference alternated between two values (dd1 and dd1)
    # derived this nth term from looking at the first few terms
    if A4 == -1:
        return -1
    if n % 2 == 0:
        n_dd1 = (n // 2) ** 2 - (n // 2)
        n_dd2 = (n - 2) * (n - 1) // 2 - n_dd1
    else:
        n_dd2 = (n // 2) ** 2 - (n // 2)
        n_dd1 = (n - 2) * (n - 1) // 2 - n_dd2
    return a1 + (n - 1) * d1 + dd1 * n_dd1 + dd2 * n_dd2


while Q:
    r, c, n = Q.popleft()
    if n > curr:
        this = odd if curr % 2 else even
        if curr == P1:
            print("Part 1:", this)
        if curr > R and curr % R == R // 2:
            if A1 == -1:
                A1 = odd if curr % 2 else even
            elif A2 == -1:
                A2 = odd if curr % 2 else even
            elif A3 == -1:
                A3 = odd if curr % 2 else even
            elif A4 == -1:
                A4 = odd if curr % 2 else even
                # A1 = a1
                # A2 = a1 + d1
                # A3 = a1 + 2 * d1 + dd1
                # A4 = a1 + 3 * d1 + 2 * dd1 + dd2
                a1 = A1
                d1 = A2 - A1
                dd1 = A3 - A1 - 2 * d1
                dd2 = A4 - A1 - 3 * d1 - 2 * dd1

                print("Part 2:", analytic(P2 // R))
                break

            if False:
                print(
                    "Step: ",
                    curr,
                    "\tBrute:",
                    this,
                    "\tAnalytic:",
                    analytic(curr // R),
                    "\t\tGoal:",
                    P2,
                    "\tAnalytic:",
                    analytic(P2 // R),
                )
        curr = n

    if n % 2 == 0:
        even += 1
    else:
        odd += 1

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nr, nc = r + dr, c + dc
        if (nr % R, nc % C) not in G and (nr, nc) not in SEEN:
            Q.append((nr, nc, n + 1))
            SEEN.add((nr, nc))

# too high
# 702322452867878
# 702322399865003
