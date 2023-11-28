import sys
from collections import defaultdict, deque

DAY = 3
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")

o2 = set(lines)
co2 = set(lines)

for i in range(len(lines[0])):
    if len(o2) > 1:
        # most common =
        o20 = {x for x in o2 if x[i] == "0"}
        o21 = {x for x in o2 if x[i] == "1"}
        if len(o20) > len(o21):
            o2 = o20
        else:
            o2 = o21

    if len(co2) > 1:
        # least common =
        co20 = {x for x in co2 if x[i] == "0"}
        co21 = {x for x in co2 if x[i] == "1"}
        if len(co20) <= len(co21):
            co2 = co20
        else:
            co2 = co21

o2 = list(o2)[0]
print(o2)
o2 = int(o2, 2)
co2 = list(co2)[0]
print(co2)
co2 = int(co2, 2)
print(o2 * co2)
