import sys
from collections import defaultdict, deque

DAY = 4
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

m = 136760
M = 595730

S = set()
for dr in range(10):
    digits = str(dr) + str(dr)

    # position 0
    for d0 in range(dr, 10):
        for d1 in range(d0, 10):
            for d2 in range(d1, 10):
                for d3 in range(d2, 10):
                    S.add(digits + "".join(str(x) for x in [d0, d1, d2, d3]))
    # position 1
    for d0 in range(dr + 1):
        for d1 in range(dr, 10):
            for d2 in range(d1, 10):
                for d3 in range(d2, 10):
                    S.add(
                        "".join(str(x) for x in [d0])
                        + digits
                        + "".join(str(x) for x in [d1, d2, d3])
                    )

    # position 2
    for d0 in range(dr + 1):
        for d1 in range(d0, dr + 1):
            for d2 in range(dr, 10):
                for d3 in range(d2, 10):
                    S.add(
                        "".join(str(x) for x in [d0, d1])
                        + digits
                        + "".join(str(x) for x in [d2, d3])
                    )

    # position 3
    for d0 in range(dr + 1):
        for d1 in range(d0, dr + 1):
            for d2 in range(d1, dr + 1):
                for d3 in range(dr, 10):
                    S.add(
                        "".join(str(x) for x in [d0, d1, d2])
                        + digits
                        + "".join(str(x) for x in [d3])
                    )

    # position 4
    for d0 in range(dr + 1):
        for d1 in range(d0, dr + 1):
            for d2 in range(d1, dr + 1):
                for d3 in range(d2, dr + 1):
                    S.add("".join(str(x) for x in [d0, d1, d2, d3]) + digits)

T = 0
for s in S:
    if m <= int(s) <= M:
        T += 1

print(T)


"""
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double)."""
