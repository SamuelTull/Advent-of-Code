import sys
from collections import defaultdict


data = "19.txt"
# data = "19test.txt"
if len(sys.argv) > 1:
    data = f"19{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()


instructions = {}
Qs = defaultdict(list)

D1, D2 = data.split("\n\n")
for line in D1.split("\n"):
    name, line = line.split("{")
    line = [x.split(":") for x in line[:-1].split(",")]
    # left as strings eg. x<10: for eval()
    instructions[name] = line


remove = lambda string, chars="{}xmas=": "".join([x for x in string if x not in chars])

for line in D2.split("\n"):
    line = line[1:-1]
    assert line.index("x") < line.index("m") < line.index("a") < line.index("s")
    line = remove(line)
    line = tuple(int(x) for x in line.split(","))
    Qs["in"].append(line)

to_check = ["in"]
while to_check:
    name = to_check.pop()
    if name in "AR":
        continue
    instr = instructions[name]
    Q = Qs[name]
    while Q:
        x, m, a, s = X = Q.pop()
        for i, where in instr[:-1]:
            if eval(i):
                Qs[where].append(X)
                to_check.append(where)
                break
        else:
            where = instr[-1][0]
            Qs[where].append(X)
            to_check.append(where)

S = 0
for X in Qs["A"]:
    S += sum(X)
print(S)
