import sys

data = "11.txt"
# data = "11test.txt"
if len(sys.argv) > 1:
    data = f"11{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

rows = data.split("\n")

G = set()
R = len(rows)
C = len(rows[0])

empty_rows = [True] * R
empty_cols = [True] * C

for r in range(R):
    for c in range(C):
        if rows[r][c] == "#":
            empty_rows[r] = False
            empty_cols[c] = False

expansion = 2  # P1: 2, P2: 1000000

dr = 0
for r in range(R):
    if empty_rows[r]:
        dr += expansion - 1
        continue
    dc = 0
    for c in range(C):
        if empty_cols[c]:
            dc += expansion - 1
            continue
        if rows[r][c] == "#":
            G.add((r + dr, c + dc))


s = 0
G = list(G)
for i in range(len(G)):
    for j in range(i + 1, len(G)):
        a0, a1 = G[i]
        b0, b1 = G[j]
        s += abs(a0 - b0) + abs(a1 - b1)
print(s)
