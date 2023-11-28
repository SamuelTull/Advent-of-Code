import sys
from collections import defaultdict

DAY = 13
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

time, info = data.split("\n")

time = int(time)
bus = [int(x) for x in info.split(",") if x != "x"]

print(time, bus)

minwait = 1e9
min_bus = None
for b in bus:
    missedby = time % b
    wait = (-time) % b
    if wait < minwait:
        minwait = wait
        min_bus = b

print(minwait * min_bus)
