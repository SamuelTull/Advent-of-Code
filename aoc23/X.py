import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

data = "X.txt"
# data = "Xtest.txt"
if len(sys.argv) > 1:
    data = f"X{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

group = data.split("\n\n")
lines = data.split("\n")

s = 0
for line in lines:
    line = line.split()


print(s)
