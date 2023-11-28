import sys
from collections import defaultdict, deque

DAY = 12
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
nodes = defaultdict(list)
for line in lines:
    a, b = line.split("-")
    nodes[a].append(b)
    nodes[b].append(a)

paths = []
q = deque([("start", "")])
while q:
    node, path = q.popleft()
    for next_node in nodes[node]:
        if next_node == "start":
            continue
        if next_node == "end":
            paths.append(path)
            continue
        if next_node.lower() == next_node and next_node in path:
            continue
        else:
            q.append((next_node, path + next_node))
print(len(paths))


lines = data.split("\n")
nodes = defaultdict(list)
for line in lines:
    a, b = line.split("-")
    nodes[a].append(b)
    nodes[b].append(a)

paths = []
q = deque([("start", "")])
while q:
    node, path = q.popleft()
    for next_node in nodes[node]:
        if next_node == "start":
            continue
        if next_node == "end":
            paths.append(path)
            continue
        if next_node.lower() == next_node and next_node in path:
            if "*" in path:
                continue
            else:
                q.append((next_node, path + "*"))
        else:
            q.append((next_node, path + next_node))
print(len(paths))
