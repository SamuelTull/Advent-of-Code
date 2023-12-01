import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

data = "1.txt"
# data = "1test.txt"
if len(sys.argv) > 1:
    data = f"1{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")


nums_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


s = 0
for line in lines:
    nums = []
    for i in range(len(line)):
        if line[i].isnumeric():
            nums.append(line[i])
    s += int(nums[0] + nums[-1])
print(s)


s = 0
for line in lines:
    nums = []
    for i in range(len(line)):
        if line[i].isnumeric():
            nums.append(line[i])
        for j in range(3, 6):
            if line[i : i + j] in nums_digit:
                nums.append(nums_digit[line[i : i + j]])
    s += int(nums[0] + nums[-1])
print(s)
