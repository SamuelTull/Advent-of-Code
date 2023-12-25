import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])


data = "24.txt"
# data = "24test.txt"
if len(sys.argv) > 1:
    data = f"24{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")

for i, line in enumerate(lines):
    line = remove(line, "@,").split()
    lines[i] = [int(x) for x in line]

N = len(lines)


def intercept(p1, p2, dxr, dyr):
    x1, y1, z1, dx1, dy1, dz1 = p1
    x2, y2, z2, dx2, dy2, dz2 = p2

    dx1 -= dxr
    dy1 -= dyr

    dx2 -= dxr
    dy2 -= dyr

    det = dx1 * dy2 - dy1 * dx2

    if det == 0:
        return None

    t1 = ((x2 - x1) * dy2 - (y2 - y1) * dx2) / det
    t2 = ((x2 - x1) * dy1 - (y2 - y1) * dx1) / det

    x = x1 + t1 * dx1
    y = y1 + t1 * dy1

    # assert math.isclose(x, x2 + t2 * dx2), abs(x - (x2 + t2 * dx2))
    # assert math.isclose(y, y2 + t2 * dy2), abs(y - (y2 + t2 * dy2))
    if t1 == t2:
        return None
    dzr = (z1 - z2 - t2 * dz2 + t1 * dz1) / (t1 - t2)
    z = z1 + t1 * (dz1 - dzr)
    return (x, y, z)


for M in [100, 500, 1000, 5000]:  # gradually increase the region we search
    for dxr in range(-M, M):  # loop through rock velocities
        for dyr in range(-M, M):  # loop through rock velocities
            intr = None
            idx = 0
            while intr is None and idx < N - 3:
                idx += 1
                intr = intercept(lines[idx - 1], lines[idx], dxr, dyr)

            if intr is None:
                continue
            if intr != intercept(lines[idx + 1], lines[idx + 2], dxr, dyr):
                continue

            print(sum(intr))

# loop through rock velocities
# all lines from "rock perspective" intercept at the point where rock is thrown from
# (using the assumption that the position exists)
# therefore X1 + t1 (V1 - RV) and  X2 + t2 (V2 - RV) should intercept
# and X1 + t3 (V1 - RV) = X3 + t4 (V3 - RV) should intercept at same place
# can loop through dx and dy and derive dz
# I am not 100% sure why but even with correct dxr, dxr, dzr None is sometimes returned
# So find the first point where intercept is not None to give fair test

# Since we know the solution exists if we find the possible R1, R2 (R = (x,y,z, dx,dy,dz))
# for two distinct pairs of trajectories, and these are equal,
# R = R1 = R2 will be valid for all the trajectories.
# This is because pairs have at most 1 vaild Ri
