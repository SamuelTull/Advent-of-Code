import sys
from collections import defaultdict, deque


def get_cost(states, goal):
    cost = 0
    for state, count in states.items():
        dist = abs(state - goal)
        cost += (dist / 2) * (1 + dist) * count
    return cost


DAY = 7
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

nums = list(map(int, data.strip().split(",")))
N = len(nums)
states = defaultdict(int)
for state in nums:
    states[state] += 1


min_cost = 1e10
for i in range(min(nums), max(nums) + 1):
    cost = get_cost(states, i)
    if cost < min_cost:
        min_cost = cost
        print(i, cost)
