import sys
from collections import defaultdict, deque

DAY = 21
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")


monkeys = {}
memo = {}

for line in lines:
    m, info = line.split(":")
    info = info.strip().split(" ")
    if len(info) == 1:
        monkeys[m] = int(info[0])
        memo[m] = int(info[0])
    else:
        monkeys[m] = info


def call(m):
    if m in memo:
        return memo[m]
    p1, op, p2 = monkeys[m]
    n1 = call(p1)
    n2 = call(p2)
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2
    if op == "/":
        return n1 / n2
    else:
        assert False, m


print(call("root"))
