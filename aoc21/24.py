import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)
import re
from tqdm import tqdm

DAY = 24
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
data = [0, 0, 0, 0]
WHO = {"w": 0, "x": 1, "y": 2, "z": 3}


def INP():
    for i in range(14):
        yield f"x{i}"


inp = INP()


def safe_float(s, val=0):
    try:
        return float(s) == val
    except ValueError:
        return False


import itertools


def generate_combinations(n):
    return ["".join(i) for i in itertools.product(map(str, range(1, 10)), repeat=n)]


for line in tqdm(lines):
    line = line.split()
    if line[0] == "inp":
        a = WHO[line[1]]
        data[a] = next(inp)
    else:
        op, a, b = line
        ai = WHO[a]
        a = data[ai]
        if b in WHO:
            b = data[WHO[b]]

        if op == "mul":
            if safe_float(a, 0) or safe_float(b, 0):
                new = "0"
            else:
                new = f"({a})*({b})"
        elif op == "add":
            new = f"({a})+({b})"
        elif op == "mod":
            if safe_float(a, 0):
                new = "0"
            else:
                new = f"({a})%({b})"
        elif op == "div":
            new = f"({a})/({b})"
        elif op == "eql":
            new = f"({a})==({b})"
        else:
            assert False, op
        if "x" not in new:
            new = float(eval(new))
        else:
            match = list(set(re.findall(r"x\d+", new)))
            n = len(match)
            if n < 6:
                new_ = new
                for i in range(n):
                    new_ = new_.replace(match[i], "1")
                new_ = eval(new_)

                for comb in generate_combinations(n):
                    new_2 = new
                    for i in range(n):
                        new_2 = new_2.replace(match[i], comb[i])
                    if eval(new_2) != new_:
                        break
                else:
                    new = float(new_)

        data[ai] = new
        # find what


data = data[-1]
match = list(set(re.findall(r"x\d+", data)))
for x0 in range(9, 0, -1):
    for x1 in range(9, 0, -1):
        for x2 in range(9, 0, -1):
            for x3 in range(9, 0, -1):
                for x4 in range(9, 0, -1):
                    for x5 in range(9, 0, -1):
                        for x6 in range(9, 0, -1):
                            for x7 in range(9, 0, -1):
                                for x8 in range(9, 0, -1):
                                    for x9 in range(9, 0, -1):
                                        for x10 in range(9, 0, -1):
                                            for x11 in range(9, 0, -1):
                                                for x12 in range(9, 0, -1):
                                                    for x13 in range(9, 0, -1):
                                                        d = eval(data)
                                                        print(d)
                                                        if eval(data) == 0:
                                                            print(
                                                                f"{x0}{x1}{x2}{x3}{x4}{x5}{x6}{x7}{x8}{x9}{x10}{x11}{x12}{x13}"
                                                            )
                                                            exit()
