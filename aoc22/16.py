import sys
from collections import defaultdict, deque

DAY = 16
PART = 1

data = str(DAY)
if False:  # change for test data debugging
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
    flow = int(line[5])
    flows[valve] = flow
    ts = []
    for i in range(10, len(line)):
        ts.append(line[i])
    flows[valve] = flow
    tunnels[valve] = ts


q = deque()
q.append([0, 0, 30, "AA", [], ["AA"]])
seen = defaultdict(lambda: -1)
best = 0
while q:
    this = q.popleft()
    tf, cf, t, curr, o, path = this
    if t == 0:
        if tf > best:
            best = tf
            bestpath = path
    else:
        score = 10000 * tf + t * cf + t
        if curr not in o and flows[curr] > 0:
            newO = sorted(o + [curr])
            if seen[curr + str(newO)] < score:
                seen[curr + str(newO)] = score
                q.append([tf + cf, cf + flows[curr], t - 1, curr, newO, ["open"]])
        for tunnel in tunnels[curr]:
            if seen[tunnel + str(o)] < score:
                seen[tunnel + str(o)] = score
                q.append([tf + cf, cf, t - 1, tunnel, o, [tunnel]])


print(best)
print(bestpath)
