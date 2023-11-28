import sys
from collections import defaultdict, deque

DAY = 2
PART = 2


data = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,1,6,23,27,1,10,27,31,1,5,31,35,2,6,35,39,1,5,39,43,1,5,43,47,2,47,6,51,1,51,5,55,1,13,55,59,2,9,59,63,1,5,63,67,2,67,9,71,1,5,71,75,2,10,75,79,1,6,79,83,1,13,83,87,1,10,87,91,1,91,5,95,2,95,10,99,2,9,99,103,1,103,6,107,1,107,10,111,2,111,10,115,1,115,6,119,2,119,9,123,1,123,6,127,2,127,10,131,1,131,6,135,2,6,135,139,1,139,5,143,1,9,143,147,1,13,147,151,1,2,151,155,1,10,155,0,99,2,14,0,0"
nums = list(map(int, data.split(",")))

idx = 0
while idx <= len(nums):
    if nums[idx] == 99:
        break
    elif nums[idx] == 1:
        nums[nums[idx + 3]] = nums[nums[idx + 1]] + nums[nums[idx + 2]]
    elif nums[idx] == 2:
        nums[nums[idx + 3]] = nums[nums[idx + 1]] * nums[nums[idx + 2]]
    else:
        assert False, nums
    idx += 4
print(nums)
print(nums[0])
