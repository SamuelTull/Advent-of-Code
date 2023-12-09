import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])

data = "9.txt"
# data = "9test.txt"
if len(sys.argv) > 1:
    data = f"9{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")

s1 = 0
s2 = 0
for line in lines:
    nums = [int(x) for x in line.split()]
    original = nums[-1]
    N = len(nums)
    steps = 0
    starts = [nums[0]]
    while (0 != min(nums[: N - steps])) or (0 != max(nums[: N - steps])):
        steps += 1
        for i in range(N - steps):
            nums[i] = nums[i + 1] - nums[i]

        starts.append(nums[0])

    # Part 1
    s1 += sum(nums[N - steps :])

    # Part 2
    curr = 0
    for i in range(len(starts) - 2, -1, -1):
        curr = starts[i] - curr
    s2 += curr
print(s1)
print(s2)
