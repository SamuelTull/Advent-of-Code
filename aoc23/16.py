import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])


def dfs(r, c, dr, dc):
    Q = deque([(r, c, dr, dc)])
    ans = set()
    SEEN = set()
    while Q:
        r, c, dr, dc = Q.popleft()
        if r < 0 or r >= R or c < 0 or c >= C:
            continue
        if (r, c, dr, dc) in SEEN:
            continue
        SEEN.add((r, c, dr, dc))
        ans.add((r, c))
        char = G[r][c]
        if char == ".":
            Q.append((r + dr, c + dc, dr, dc))
        elif char == "/":
            Q.append((r - dc, c - dr, -dc, -dr))
        elif char == "\\":
            Q.append((r + dc, c + dr, dc, dr))
        elif char == "|":
            if dc != 0:
                Q.append((r - 1, c, -1, 0))
                Q.append((r + 1, c, 1, 0))
            else:
                Q.append((r + dr, c + dc, dr, dc))
        else:
            assert char == "-"
            if dr != 0:
                Q.append((r, c - 1, 0, -1))
                Q.append((r, c + 1, 0, 1))
            else:
                Q.append((r + dr, c + dc, dr, dc))
    return len(ans)


data = "16.txt"
# data = "16test.txt"
if len(sys.argv) > 1:
    data = f"16{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

G = data.split("\n")
R = len(G)
C = len(G[0])

ans = dfs(0, 0, 0, 1)
print(ans)

for i in range(max(C, R)):
    ans = max(
        ans,
        dfs(0, i, 1, 0),
        dfs(R - 1, i, -1, 0),
        dfs(i, 0, 0, 1),
        dfs(i, C - 1, 0, -1),
    )
print(ans)
