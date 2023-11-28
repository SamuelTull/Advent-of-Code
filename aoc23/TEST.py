import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

data = "TEST.txt"
# data = "TESTtest.txt"
if len(sys.argv) > 1:
    data = f"TEST{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")
