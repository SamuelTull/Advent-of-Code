import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

data = "4.txt"
# data = "4test.txt"
if len(sys.argv) > 1:
    data = f"4{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")
s = 0
total = defaultdict(int)

for i, line in enumerate(lines):
    my, nums = line.split(":")[1].split("|")
    my, nums = set(map(int, my.split())), set(map(int, nums.split()))
    corr = len(my & nums)
    if corr > 0:
        s += 2 ** (corr - 1)  # P1
    total[i] += 1  # original card
    for di in range(1, corr + 1):
        total[i + di] += total[i]  # P2

print(s)
print(sum(total.values()))
