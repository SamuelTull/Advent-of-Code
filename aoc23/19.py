import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)


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
    instructions[name] = line

Qs["in"].append(((1, 4000), (1, 4000), (1, 4000), (1, 4000)))

to_check = ["in"]
while to_check:
    name = to_check.pop()
    if name in "AR":
        continue
    Q = Qs[name]
    while Q:
        X = Q.pop()
        for inst, where in instructions[name][:-1]:
            if "<" in inst:
                i, val = inst.split("<")
                i = ["x", "m", "a", "s"].index(i)
                val = int(val)

                if val <= X[i][0]:
                    # all stays - go to next instruction
                    continue
                elif val > X[i][1]:
                    # all goes to "where"
                    Qs[where].append(X)
                    to_check.append(where)
                    break
                else:
                    # some goes to "where", some stays
                    NX = list(X)
                    NX[i] = (NX[i][0], val - 1)
                    Qs[where].append(tuple(NX))
                    to_check.append(where)
                    X = list(X)
                    X[i] = (val, X[i][1])
                    X = tuple(X)

            else:  # ">"
                i, val = inst.split(">")
                i = ["x", "m", "a", "s"].index(i)
                val = int(val)

                if val >= X[i][1]:
                    continue
                elif val < X[i][0]:
                    # all goes to "where"
                    Qs[where].append(X)
                    to_check.append(where)
                    break
                else:
                    NX = list(X)
                    NX[i] = (val + 1, NX[i][1])
                    Qs[where].append(tuple(NX))
                    to_check.append(where)
                    X = list(X)
                    X[i] = (X[i][0], val)
                    X = tuple(X)
        else:
            where = instructions[name][-1][0]
            Qs[where].append(X)
            to_check.append(where)

S = 0j
for x, m, a, s in Qs["A"]:
    lx = x[1] - x[0] + 1
    lm = m[1] - m[0] + 1
    la = a[1] - a[0] + 1
    ls = s[1] - s[0] + 1
    S += lx * lm * la * ls
print(S)
