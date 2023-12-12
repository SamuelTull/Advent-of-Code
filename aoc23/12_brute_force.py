import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])


def valid(a, b):
    return b == [len(x) for x in a.split(".") if x != ""]


def solve(a, b, i):
    if i == len(a):
        return valid(a, b)
    if a[i] in ".#":
        return solve(a, b, i + 1)
    count = 0
    for s in "#.":
        a = a[:i] + s + a[i + 1 :]
        count += solve(a, b, i + 1)
    a = a[:i] + "?" + a[i + 1 :]
    return count


data = "12.txt"
# data = "12test.txt"
if len(sys.argv) > 1:
    data = f"12{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")

s = 0
for line in lines:
    a, b = line.split()
    b = list(map(int, b.split(",")))
    s += solve(a, b, 0)
print(s)
