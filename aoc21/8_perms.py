import sys
from collections import defaultdict, deque
from itertools import permutations


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

digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

for line in lines:
    data, target = line.split("|")
    data = ["".join(sorted(s)) for s in data.split()]
    target = ["".join(sorted(s)) for s in target.split()]

    for t in target:
        if len(t) in [2, 3, 4, 7]:
            p1 += 1

    for d in data:
        if len(d) == 3:
            acf = d
        elif len(d) == 4:
            bcdf = d

    mapping = {}
    found = False
    for a, c, f in permutations(acf):
        for b, d in permutations(bcdf, 2):
            if len(set([a, b, c, d, f])) != 5:
                continue
            for e, g in permutations("abcdefg", 2):
                if found:
                    break
                if len(set([a, b, c, d, e, f, g])) != 7:
                    continue

                mapping["a"] = a
                mapping["c"] = c
                mapping["f"] = f
                mapping["b"] = b
                mapping["d"] = d
                mapping["e"] = e
                mapping["g"] = g
                found = True

                for digit in digits.values():
                    if "".join(sorted(mapping[char] for char in digit)) not in data:
                        found = False
                        break

    digit = ""
    for t in target:
        for i, d in digits.items():
            if "".join(sorted(mapping[char] for char in d)) == t:
                digit += str(i)
                break
    print(digit)
    p2 += int(digit)

print(p1)
print(p2)
