import sys
from collections import defaultdict, deque
from utils import get_time

DAY = 19
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
Blueprints = {}
for idx in range(len(lines)):
    blueprint = [int(lines[idx].split(" ")[i]) for i in [6, 12, 18, 21, 27, 30]]
    Blueprints[idx + 1] = blueprint


def append(T, o, c, ob, ro, rc, rob, total):
    # cap robots at max needed as no point buildng more than we can spend each turn
    # cap resources at max we can spend each turn
    ro = min(ro, MaxOre)
    rc = min(rc, CostObs2)
    rob = min(rob, CostGeo2)
    o = min(o, (MaxOre) * (T - 1) - ro * (T - 2))
    c = min(c, (CostObs2) * (T - 1) - rc * (T - 2))
    ob = min(ob, (CostGeo2) * (T - 1) - rob * (T - 2))
    state = (T, o, c, ob, ro, rc, rob)
    if state not in SEEN or total > SEEN[state]:
        SEEN[state] = total
        Q.append([state, total])


@get_time
def solve():
    best = 0
    while Q:
        state, total = Q.pop()
        best = max(best, total)
        T, o, c, ob, ro, rc, rob = state
        if T == 2:
            if o >= CostGeo1 and ob >= CostGeo2:
                # buy one more obs robot
                best = max(best, total + 1)
            continue
        # fmt: off
        append(T - 1, o + ro, c + rc, ob + rob, ro, rc, rob, total)  # do nothing
        if o >= CostOre:
            append(T - 1, o + ro - CostOre, c + rc, ob + rob, ro + 1, rc, rob, total) # buy ore
        if o >= CostClay:
            append(T - 1, o + ro - CostClay, c + rc, ob + rob, ro, rc + 1, rob, total)  # buy clay
        if o >= CostObs1 and c >= CostObs2:
            append(T - 1,o + ro - CostObs1,c + rc - CostObs2,ob + rob,ro,rc,rob + 1,total)  # buy obs
        if o >= CostGeo1 and ob >= CostGeo2:
            append(T - 1,o + ro - CostGeo1,c + rc,ob + rob - CostGeo2,ro,rc,rob,total + T - 1)  # buy geo
        # fmt: on
    return best


P1 = 0
for idx, blueprint in Blueprints.items():
    CostOre, CostClay, CostObs1, CostObs2, CostGeo1, CostGeo2 = blueprint
    MaxOre = max(CostOre, CostClay, CostObs1, CostGeo1)
    Q = deque([[(24, 0, 0, 0, 1, 0, 0), 0]])
    SEEN = {(24, 0, 0, 0, 1, 0, 0): 0}
    best = solve()
    P1 += idx * best
    print(idx, blueprint, best, "P1:", P1)
P2 = 1
for idx, blueprint in Blueprints.items():
    if idx > 3:
        continue
    CostOre, CostClay, CostObs1, CostObs2, CostGeo1, CostGeo2 = blueprint
    MaxOre = max(CostOre, CostClay, CostObs1, CostGeo1)
    Q = deque([[(32, 0, 0, 0, 1, 0, 0), 0]])
    SEEN = {(32, 0, 0, 0, 1, 0, 0): 0}
    best = solve()
    P2 *= best
    print(idx, blueprint, best, "P2:", P2)

print()
print("P1", P1)
print("P2", P2)
