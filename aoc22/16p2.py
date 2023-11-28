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

flows = {}
tunnels = {}

for line in lines:
    line = line.replace("=", " ").replace(";", "").replace(",", "").split(" ")
    valve = line[1]
    ts = []
    for i in range(10, len(line)):
        ts.append(line[i])
    flows[valve] = int(line[5])
    tunnels[valve] = ts


shortestpaths = {}
for x in flows:
    if x != "AA" and flows[x] == 0:
        continue
    shortestpaths[x] = {}
    q = deque([(0, x)])
    seen = {x}
    while q:
        d, curr = q.popleft()
        for neighbour in tunnels[curr]:
            if neighbour in seen:
                continue
            if flows[neighbour] > 0:
                shortestpaths[x][neighbour] = d + 1
            seen.add(neighbour)
            q.append((d + 1, neighbour))


q = deque()
q.append(["AA", "AA", 26, 26, {"AA"}, 0])
seen = defaultdict(int)
best = 0
while q:
    c0, c1, t0, t1, visited, total = q.pop()
    if total > best:
        best = total
        print(f"Best={best}, len(q)={len(q)}")

    for destination in shortestpaths:
        if destination in visited:
            continue
        # move player 1 to dest
        dist = shortestpaths[c0][destination]
        if t0 > dist + 2:
            newTotal = total + (t0 - dist - 1) * flows[destination]
            newVisited = visited | {destination}
            if newTotal > seen[str(sorted(newVisited))]:
                seen[str(sorted(newVisited))] = newTotal
                q.append(
                    [
                        destination,
                        c1,
                        t0 - dist - 1,
                        t1,
                        newVisited,
                        newTotal,
                    ]
                )
        # move player 2 to dest
        # if (c0, t0) == (c1, t1): continue # seems faster not to bother checking
        dist = shortestpaths[c1][destination]
        if t1 > dist + 2:
            newTotal = total + (t1 - dist - 1) * flows[destination]
            newVisited = visited | {destination}
            if newTotal > seen[str(sorted(newVisited))]:
                seen[str(sorted(newVisited))] = newTotal
                q.append(
                    [
                        c0,
                        destination,
                        t0,
                        t1 - dist - 1,
                        newVisited,
                        newTotal,
                    ]
                )
print(best)
