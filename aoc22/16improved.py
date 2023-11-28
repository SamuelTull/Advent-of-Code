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

# q = deque()
# q.append(
#     [
#         caves.index("AA"),  # current player
#         30,  # time player
#         0,  # visited (bitwise)
#         0,  # total
#     ]
# )
# seen = defaultdict(int)
# best = 0
# while q:
#     c0, t0, visited, total = q.popleft()
#     if total > best:
#         best = total
#         print(f"Best={best}, len(q)={len(q)}")
#     for i in IDs:
#         if 1 << i & visited:  # check if visited already
#             continue
#         dist = D[c0][i]
#         if t0 > dist + 1:  # check time to travel there and turn on
#             newTotal = total + (t0 - dist - 1) * flows[i]
#             newVisited = visited | 1 << i
#             if newTotal > seen[(i, newVisited)]:
#                 seen[(i, newVisited)] = newTotal
#                 q.append(
#                     [
#                         i,
#                         t0 - dist - 1,
#                         newVisited,
#                         newTotal,
#                     ]
#                 )
# print(best)


import functools


@functools.lru_cache(maxsize=None)
def p1(c, t, visited):
    # at c with time t and visited
    # what can we gain
    if t == 0:
        return 0
    maxGain = 0
    for i in IDs:
        if 1 << i & visited:
            continue
        t -= D[c][i] + 1
        if t > 0:
            visited |= 1 << i
            gain = t * flows[i]
            maxGain = max(maxGain, gain + p1(i, t, visited))
            visited ^= 1 << i
        t += D[c][i] + 1
    return maxGain


@functools.lru_cache(maxsize=None)
def p2(c1, c2, t1, t2, visited):
    maxGain = 0
    for i in IDs:
        if 1 << i & visited:
            continue
        # c1 to destination
        dist1 = D[c1][i]
        if t1 > dist1 + 1:
            gain = (t1 - dist1 - 1) * flows[i]
            t1 -= dist1 + 1
            visited |= 1 << i
            maxGain = max(maxGain, gain + p2(i, c2, t1, t2, visited))
            t1 += dist1 + 1
            visited ^= 1 << i

        # c2 to destination
        dist2 = D[c2][i]
        if t2 > dist2 + 1:
            gain = (t2 - dist2 - 1) * flows[i]
            t2 -= dist2 + 1
            visited |= 1 << i
            maxGain = max(maxGain, gain + p2(c1, i, t1, t2, visited))
            t2 += dist2 + 1
            visited ^= 1 << i
    return maxGain


@functools.lru_cache(maxsize=None)
def p2_v1(c1, c2, t1, t2, visited):
    if t1 < t2:
        c1, c2 = c2, c1
        t1, t2 = t2, t1

    maxGain = 0
    for i in IDs:
        if 1 << i & visited:
            continue
        # c1 to destination
        dist1 = D[c1][i]
        if t1 > dist1 + 1:
            gain = (t1 - dist1 - 1) * flows[i]
            t1 -= dist1 + 1
            visited |= 1 << i
            maxGain = max(maxGain, gain + p2_v1(i, c2, t1, t2, visited))
            t1 += dist1 + 1
            visited ^= 1 << i

        # c2 to destination
        dist2 = D[c2][i]
        if t2 > dist2 + 1:
            gain = (t2 - dist2 - 1) * flows[i]
            t2 -= dist2 + 1
            visited |= 1 << i
            maxGain = max(maxGain, gain + p2_v1(c1, i, t1, t2, visited))
            t2 += dist2 + 1
            visited ^= 1 << i
    return maxGain


@functools.lru_cache(maxsize=None)
def p2_v3(c1, c2, t1, t2, visited):
    maxGain = 0
    for i in IDs:
        if 1 << i & visited:
            continue
        # c1 to destination
        dist1 = D[c1][i]
        if t1 > dist1 + 1:
            gain = (t1 - dist1 - 1) * flows[i]
            t1 -= dist1 + 1
            visited |= 1 << i
            if t1 > t2:
                maxGain = max(maxGain, gain + p2_v3(i, c2, t1, t2, visited))
            else:
                maxGain = max(maxGain, gain + p2_v3(c2, i, t2, t1, visited))
            t1 += dist1 + 1
            visited ^= 1 << i

        # c2 to destination
        dist2 = D[c2][i]
        if t2 > dist2 + 1:
            gain = (t2 - dist2 - 1) * flows[i]
            t2 -= dist2 + 1
            visited |= 1 << i
            if t1 > t2:
                maxGain = max(maxGain, gain + p2_v3(c1, i, t1, t2, visited))
            else:
                maxGain = max(maxGain, gain + p2_v3(i, c1, t2, t1, visited))
            t2 += dist2 + 1
            visited ^= 1 << i
    return maxGain


@functools.lru_cache(maxsize=None)
def p2_v2(c1, c2, t1, t2, visited):
    maxGain = 0
    for i in IDs:
        if 1 << i & visited:
            continue
        # c1 to destination
        dist1 = D[c1][i]
        dist2 = D[c2][i]
        if t1 > dist1 + 1:
            gain = (t1 - dist1 - 1) * flows[i]
            t1 -= dist1 + 1
            visited |= 1 << i
            if t1 > t2:
                maxGain = max(maxGain, gain + p2_v2(i, c2, t1, t2, visited))
            else:
                maxGain = max(maxGain, gain + p2_v2(c2, i, t2, t1, visited))
            t1 += dist1 + 1
            visited ^= 1 << i
        elif t2 > dist2 + 1:
            gain = (t2 - dist2 - 1) * flows[i]
            t2 -= dist2 + 1
            visited |= 1 << i
            if t1 > t2:
                maxGain = max(maxGain, gain + p2_v2(c1, i, t1, t2, visited))
            else:
                maxGain = max(maxGain, gain + p2_v2(i, c1, t2, t1, visited))
            t2 += dist2 + 1
            visited ^= 1 << i

    return maxGain


AA = caves.index("AA")
# print(p1(AA, 30, 0))
import time

start = time.time()
print(p2(AA, AA, 26, 26, 0))
print(time.time() - start)


# start = time.time()
# print(p2_v1(AA, AA, 26, 26, 0))
# print(time.time() - start)


# start = time.time()
# print(p2_v2(AA, AA, 26, 26, 0))
# print(time.time() - start)


# start = time.time()
# print(p2_v3(AA, AA, 26, 26, 0))
# print(time.time() - start)


# s = 0
# for i in IDs:
#     s += 1 << i
# p2 = 0
# for i in range(s):
#     p2 = max(p2, p1(AA, 26, i) + p1(AA, 26, s ^ i))
