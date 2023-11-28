import sys
from collections import defaultdict, deque
from queue import PriorityQueue

DAY = 24
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()
data = [[x for x in line.strip()[1:-1]] for line in data.split("\n")[1:-1]]
H = len(data)
W = len(data[0])
for LCM in range(H, H * W + 1):
    if LCM % W == 0 and LCM % H == 0:
        break
start = (-1, 0)
end = (H, W - 1)


def add(r, c, state, t):
    tidx = t % LCM
    if (r, c, state) not in SEEN[tidx]:
        SEEN[tidx].add((r, c, state))
        Q.append((t, r, c, state))


Q = deque([(0, -1, 0, 0)])
SEEN = {i: set() for i in range(LCM)}
T = -1
while Q:
    t, r, c, state = Q.popleft()
    if r == H:
        if state == 2:
            print("P2", t)
            break
        else:
            state = 1
    elif r == -1 and state == 1:
        state = 2

    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]:
        nr, nc = r + dr, c + dc
        if (nr, nc) == (-1, 0) or (nr, nc) == (H, W - 1):
            add(nr, nc, state, t + 1)
        elif (
            (0 <= nr < H and 0 <= nc < W)
            or (nr, nc) == (-1, 0)
            or (nr, nc) == (H, W - 1)
        ):
            for char, tr, tc in [("^", -1, 0), ("v", 1, 0), (">", 0, 1), ("<", 0, -1)]:
                if data[(nr - tr * (t + 1)) % H][(nc - tc * (t + 1)) % W] == char:
                    break
            else:
                add(nr, nc, state, t + 1)
