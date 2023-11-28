import sys
from collections import defaultdict

DAY = 7
PART = 1 + 2

data = str(DAY)
if len(sys.argv) > 1:
    if sys.argv[1] in ["0", "test"]:
        data = str(DAY) + "test"
    else:
        data = str(DAY) + sys.argv[1]

with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
rules = defaultdict(list)


for line in lines:
    outer, inner = line.split("contain")
    outer = outer.strip().split(" ")
    outer = outer[0] + outer[1]
    inners = []
    for i in inner.strip().split(","):
        i = i.strip().split(" ")
        num = i[0]
        bag = i[1] + i[2]
        if num != "no":
            rules[outer].append((int(num), bag))


old = set()
new = {"shinygold"}
while new != old:
    old = {x for x in new}
    for outer, inners in rules.items():
        for num, inner in inners:
            if inner in new:
                new.add(outer)
print("P1", len(new) - 1)


def count(bag):
    s = 0
    if bag in rules:
        for num, inner in rules[bag]:
            s += num * count(inner)
        return s + 1
    else:
        return 1


print(count("shinygold") - 1)
