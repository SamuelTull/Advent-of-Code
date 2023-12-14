import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])


def NORTH(G):
    G2 = set()
    for r in range(R):
        for c in range(C):
            if (r, c) in G:
                dr = 0
                while (
                    r - dr - 1 >= 0
                    and (r - dr - 1, c) not in walls
                    and (r - dr - 1, c) not in G2
                ):
                    dr += 1
                G2.add((r - dr, c))
    return G2


def SOUTH(G):
    G2 = set()
    for r in range(R - 1, -1, -1):
        for c in range(C):
            if (r, c) in G:
                dr = 0
                while (
                    r + dr + 1 < R
                    and (r + dr + 1, c) not in walls
                    and (r + dr + 1, c) not in G2
                ):
                    dr += 1
                G2.add((r + dr, c))
    return G2


def EAST(G):
    G2 = set()
    for c in range(C - 1, -1, -1):
        for r in range(R):
            if (r, c) in G:
                dc = 0
                while (
                    c + dc + 1 < C
                    and (r, c + dc + 1) not in walls
                    and (r, c + dc + 1) not in G2
                ):
                    dc += 1
                G2.add((r, c + dc))
    return G2


def WEST(G):
    G2 = set()
    for c in range(C):
        for r in range(R):
            if (r, c) in G:
                dc = 0
                while (
                    c - dc - 1 >= 0
                    and (r, c - dc - 1) not in walls
                    and (r, c - dc - 1) not in G2
                ):
                    dc += 1
                G2.add((r, c - dc))
    return G2


def spin(G):
    G = NORTH(G)
    G = WEST(G)
    G = SOUTH(G)
    return EAST(G)


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


print(ans(NORTH(G)))

# only need states after complete spins - if the same after N/S/W then will be the same after E
# wouldnt need to run the extra spins, if kept track of G
# would just need to find G[states[hash_g] + remaining])
# but this is fast enough

states = {}
i = 0
while True:
    i += 1
    G = spin(G)
    hash_g = tuple(G)
    if hash_g in states:
        cycle_len = i - states[hash_g]
        goal = 1000000000
        extra_cycles = (goal - i) // cycle_len
        remaining = goal - (i + extra_cycles * cycle_len)
        for _ in range(remaining):
            G = spin(G)
        print(ans(G))
        break
    states[hash_g] = i
