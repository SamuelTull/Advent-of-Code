import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])

data = "data.txt"
# data = "test.txt"

with open(data) as f:
    data = f.read().strip()

groups = data.split("\n\n") # if the lines are grouped - and seperated by a blank space
lines = data.split("\n")

m = defaultdict(int)

for line in lines: 
    line = line.split() # splits by blank space
    



