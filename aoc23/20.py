import sys
from collections import deque
from math import lcm

data = "20.txt"
# data = "20test.txt"
if len(sys.argv) > 1:
    data = f"20{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

nodes = {}
child = {}
inputs = {}

lines = data.split("\n")

for line in lines:
    this, other = line.split(" -> ")
    other = [o.strip() for o in other.split(",")]
    if this[0] == "%":
        nodes[this[1:]] = False
        child[this[1:]] = other
    elif this[0] == "&":
        nodes[this[1:]] = "&"
        child[this[1:]] = other
    else:
        S = other

for node in nodes:
    if nodes[node] != "&":
        continue
    for node2 in nodes:
        if node == node2:
            continue
        if node in child[node2]:
            inputs[node] = inputs.get(node, {})
            inputs[node][node2] = False


goal = "rx"
goal_parent = [x for x in nodes if goal in child[x]][0]
goal_grandparents = [x for x in nodes if goal_parent in child[x]]
counts = {p: 0 for p in goal_grandparents}
cycles = {}


n_low = n_hi = 0
for repeat in range(1, 200000):
    Q = deque((s, False) for s in S)  # node, pulse == high
    n_low += 1
    while Q:
        s, hi = Q.popleft()
        if hi:
            n_hi += 1
        else:
            n_low += 1

        if s in goal_grandparents and inputs[goal_parent][s]:
            counts[s] += 1
            if s not in cycles:
                cycles[s] = repeat
            else:
                assert cycles[s] * counts[s] == repeat

        if s not in nodes:
            continue

        if nodes[s] == "&":
            if all(inputs[s].values()):
                for s2 in child[s]:
                    if s2 in inputs:
                        inputs[s2][s] = False
                    Q.append((s2, False))
            else:
                for s2 in child[s]:
                    if s2 in inputs:
                        inputs[s2][s] = True
                    Q.append((s2, True))
        else:
            if hi:
                continue
            nodes[s] = not nodes[s]
            for s2 in child[s]:
                if s2 in inputs:
                    inputs[s2][s] = nodes[s]
                Q.append((s2, nodes[s]))
    if repeat == 1000:
        print("P1", n_low * n_hi)

    if all(count > 10 for count in counts.values()):
        print("P2", lcm(*cycles.values()))
        break
