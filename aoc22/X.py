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

lines = data.split("\n")
nums = [int(x) for x in lines]
N = len(lines)
s = 0
S = {}
