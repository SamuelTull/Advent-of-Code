import sys
from collections import defaultdict, deque
import random
from copy import deepcopy
from itertools import permutations

data = "25.txt"
# data = "25test.txt"
if len(sys.argv) > 1:
    data = f"25{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")

G = defaultdict(set)

for line in lines:
    line = line.split()
    a, B = line[0][:-1], line[1:]
    for b in B:
        G[a].add(b)
        G[b].add(a)

visited = defaultdict(int)
import time

sss = time.time()
for _ in range(1000):
    start = random.choice(list(G.keys()))
    goal = random.choice(list(G.keys()))
    Q = deque([(start, {start})])
    seen = {start}
    while Q:
        x, path = Q.popleft()
        if x == goal:
            break
        for y in G[x]:
            if y not in seen:
                Q.append((y, path | {y}))
                seen.add(y)
    for x in path:
        visited[x] += 1

print(time.time() - sss)
cut_nodes = {
    x[0] for x in sorted(visited.items(), key=lambda x: (x[1], x[0]), reverse=True)[:6]
}

G_copy = deepcopy(G)

for a, b, c, d, e, f in permutations(cut_nodes, 6):
    if not a > c > e:  # avoid repeats
        continue
    if a < b or b not in G[a]:
        continue
    if c < d or d not in G[c]:
        continue
    if e < f or f not in G[e]:
        continue
    G = deepcopy(G_copy)
    G[a].remove(b)
    G[b].remove(a)
    G[c].remove(d)
    G[d].remove(c)
    G[e].remove(f)
    G[f].remove(e)
    Q = deque([a])
    seen = {a}
    while Q:
        x = Q.popleft()
        for y in G[x]:
            if y not in seen:
                seen.add(y)
                Q.append(y)
    print(len(seen) * (len(G) - len(seen)))
