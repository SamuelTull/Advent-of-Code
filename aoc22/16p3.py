import sys
from collections import defaultdict, deque

DAY = 16
PART = 2

data = str(DAY)
if False:
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]

with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")

caves = []
flows = []
tunnels = []

for line in lines:
    val, tuns = (
        line.replace("=", " ")
        .replace(";", "")
        .replace(",", "")
        .replace("valves", "valve")
        .split("valve")
    )
    ID, flow = val.split(" ")[1], val.split(" ")[5]
    caves.append(ID)
    flows.append(int(flow))
    tunnels.append(tuns.strip().split(" "))

N = len(caves)
D = [[1e10 for _ in range(N)] for _ in range(N)]
for i in range(len(caves)):
    D[i][i] = 0
    for tunnel in tunnels[i]:
        D[i][caves.index(tunnel)] = 1

for r in range(N):
    for p in range(N):
        for q in range(N):
            D[p][q] = min(D[p][q], D[p][r] + D[r][q])

IDs = [i for i in range(N) if flows[i] > 0]

maxflow = max(flows)


q = deque()
q.append(
    [
        caves.index("AA"),  # current player
        caves.index("AA"),  # current elephant
        26,  # time player
        26,  # time elephant
        0,  # visited (bitwise)
        0,  # total
    ]
)
seen = defaultdict(int)
best = 0
while q:
    c0, c1, t0, t1, visited, total = q.popleft()
    if total > best:
        best = total
        # print(f"Best={best}, len(q)={len(q)}")

    for i in IDs:
        if 1 << i & visited:
            continue
        # move player 1 to destination
        dist = D[c0][i]
        if t0 > dist + 1:
            newTotal = total + (t0 - dist - 1) * flows[i]
            newVisited = visited | 1 << i
            if newTotal > seen[newVisited]:
                seen[newVisited] = newTotal
                q.append(
                    [
                        i,
                        c1,
                        t0 - dist - 1,
                        t1,
                        newVisited,
                        newTotal,
                    ]
                )

    if (c0, t0) == (c1, t1):
        continue  # seems faster not to bother checking

    # move player 2 to destination
    for i in IDs:
        if 1 << i & visited:
            continue
        dist = D[c1][i]
        if t1 > dist + 1:
            newTotal = total + (t1 - dist - 1) * flows[i]
            newVisited = visited | 1 << i
            if newTotal > seen[newVisited]:
                seen[newVisited] = newTotal
                q.append(
                    [
                        c0,
                        i,
                        t0,
                        t1 - dist - 1,
                        newVisited,
                        newTotal,
                    ]
                )
print(best)
