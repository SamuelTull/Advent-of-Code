import sys
from collections import defaultdict, deque

DAY = 21
PART = 2

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")


monkeys = {}
for line in lines:
    m, info = line.split(":")
    monkeys[m] = info.strip().split(" ")


def call(m):
    info = monkeys[m]
    if len(info) == 1:
        return info[0]
    p1, op, p2 = monkeys[m]
    n1 = call(p1)
    n2 = call(p2)
    out = f"({n1}) {op} ({n2})"
    return out


p1, _, p2 = monkeys["root"]
monkeys["humn"] = "x"
Eq1 = call(p1)
Eq2 = call(p2)
import sympy

print("P2", sympy.solve(f"Eq( {Eq1} - {Eq2},0)"))

"""
def secant_method(x0=0, x1=1e9, tol=1e-8):
    while True:
        if abs(x0 - x1) < tol:
            print("Found!", x0)
            return
        x2 = x1 - f(x1) * (x1 - x0) / float(f(x1) - f(x0))
        print("Step:", (x0, x1, x2))
        x0, x1 = x1, x2


def f(x):
    return eval(f"{Eq1} - {Eq2}")


secant_method()"""
