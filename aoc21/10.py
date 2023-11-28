import sys
from collections import defaultdict, deque

DAY = 10
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")

score = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

score_p2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

map_close = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
map_open = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

p1 = 0
p2 = []
for line in lines:
    fail = False
    open_ = ""
    for c in line:
        if c in map_open:
            open_ += c
        else:
            if open_[-1] != map_close[c]:
                fail = True
                p1 += score[c]
                break
            open_ = open_[:-1]

    if not fail:
        s = 0
        for c in open_[::-1]:
            s *= 5
            s += score_p2[map_open[c]]
        p2.append(s)

print(p1)
p2.sort()
print(p2[len(p2) // 2])
