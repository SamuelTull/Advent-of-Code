import sys
from collections import defaultdict, deque

DAY = 19
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
# groups = data.split("\n\n")
# grid = [[x for x in line.strip()] for line in data.split("\n")]
# lines = [int(x) for x in lines]
# lines = [x.replace("-", ",").split(",") for x in lines]
# lines = [x.split(" ") for x in lines]
# integers = map(int, line.split(","))
# nums = [int(x) for x in data.strip().split(",")]
# counts = defaultdict(int)
# for num in [int(x) for x in data.strip().split(",")]:
#     counts[num] += 1
