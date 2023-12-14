import sys

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])


def roll(G, dr, dc):
    G2 = set()
    range_r = {-1: range(R), 0: range(R), 1: range(R - 1, -1, -1)}[dr]
    range_c = {-1: range(C), 0: range(C), 1: range(C - 1, -1, -1)}[dc]
    for r in range_r:
        for c in range_c:
            if (r, c) in G:
                rr, cc = r, c
                while (
                    0 <= rr + dr < R
                    and 0 <= cc + dc < C
                    and (rr + dr, cc + dc) not in walls
                    and (rr + dr, cc + dc) not in G2
                ):
                    rr += dr
                    cc += dc
                G2.add((rr, cc))
    return G2


def spin(G):
    G = roll(G, -1, 0)
    G = roll(G, 0, -1)
    G = roll(G, 1, 0)
    G = roll(G, 0, 1)
    return G


def ans(G):
    s = 0
    for r in range(R):
        for c in range(C):
            if (r, c) in G:
                s += R - r
    return s


data = "14.txt"
# data = "14test.txt"
if len(sys.argv) > 1:
    data = f"14{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()
lines = data.split("\n")

G = set()
G2 = set()
walls = set()
R = len(lines)
C = len(lines[0])
s = 0

for r, line in enumerate(lines):
    for c, char in enumerate(line):
        if char == "#":
            walls.add((r, c))
        elif char == "O":
            G.add((r, c))


print(ans(roll(G, -1, 0)))

# only need to track states after complete spins
# if the same after N/S/W then will be the same after E
# dont technically need to run the extra spins
# just need to find G[states[hash_g] + remaining])
# but this is fast enough

goal = 1000000000
i = 0
states = {}
while i < goal:
    i += 1
    G = spin(G)
    hash_g = tuple(G)
    if hash_g in states:
        cycle_len = i - states[hash_g]
        extra_spins = (goal - i) // cycle_len
        i += extra_spins * cycle_len
        states = {}
    states[hash_g] = i

print(ans(G))
