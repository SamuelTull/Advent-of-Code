import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])


@functools.lru_cache(maxsize=None)
def solve(a, b):
    if a == "":
        return b == ""
    if a[0] == ".":
        return solve(a[1:], b)
    if a[0] == "#":
        if not b:
            return 0
        b0, b = b.split(",", 1) if "," in b else (b, "")
        b0 = int(b0)
        if len(a) < b0 or "." in a[:b0]:
            return 0
        elif len(a) == b0:
            return solve(a[b0:], b)
        else:
            char = a[b0]
            if char == "#":
                return 0
            else:
                return solve(a[b0 + 1 :], b)
    return solve(a[1:], b) + solve("#" + a[1:], b)


data = "12.txt"
# data = "12test.txt"
if len(sys.argv) > 1:
    data = f"12{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")
s = 0
for i, line in enumerate(lines):
    a, b = line.split()
    a = a + "?" + a + "?" + a + "?" + a + "?" + a
    b = b + "," + b + "," + b + "," + b + "," + b
    s += solve(a, b)
    # solve.cache_clear()
print(s)
