import sys
from collections import defaultdict, deque


def add(a, b):
    return "".join(x for x in sorted(set(a for a in a) | set(b for b in b)))


def sub(a, b):
    return "".join(x for x in sorted(set(a for a in a) - set(b for b in b)))


def and_(a, b):
    return "".join(x for x in sorted(set(a for a in a) & set(b for b in b)))


DAY = 8
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
p1 = 0
p2 = 0
for line in lines:
    data, target = line.split("|")
    data = ["".join(sorted(s)) for s in data.split()]
    target = ["".join(sorted(s)) for s in target.split()]

    for t in target:
        if len(t) in [2, 3, 4, 7]:
            p1 += 1
    values = ["" for _ in range(10)]
    horizontal = "abcdefg"
    corners = "abcdefg"
    counts = defaultdict(int)
    for d in data:
        for char in d:
            counts[char] += 1
        if len(d) == 2:
            values[1] = d
        elif len(d) == 3:
            values[7] = d
        elif len(d) == 4:
            values[4] = d
        elif len(d) == 7:
            values[8] = d
        elif len(d) == 5:
            horizontal = and_(horizontal, d)
        elif len(d) == 6:
            corners = and_(corners, d)
    assert len(horizontal) == 3
    assert len(corners) == 4

    values[5] = add(horizontal, corners)

    e = "".join(char for char in counts if counts[char] == 4)
    b = "".join(char for char in counts if counts[char] == 6)
    dg = "".join(char for char in counts if counts[char] == 7)
    ac = "".join(char for char in counts if counts[char] == 8)
    f = "".join(char for char in counts if counts[char] == 9)
    d = sub(dg, corners)
    g = sub(dg, d)
    c = sub(ac, horizontal)
    a = sub(ac, c)

    print(and_(corners, horizontal), add(a, g))
    assert and_(corners, horizontal) == add(a, g)

    values[9] = sub(values[8], e)
    values[0] = sub(values[8], d)
    values[6] = sub(values[8], c)

    values[2] = "".join(sorted([a, c, d, e, g]))
    values[3] = sub(values[9], b)

    digit = ""
    for t in target:
        digit += str(values.index(t))
    print(digit)
    p2 += int(digit)

print(p1)
print(p2)
