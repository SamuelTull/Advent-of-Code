import sys
from collections import defaultdict, deque

DAY = 6
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

states = defaultdict(int)
for state in data.strip().split(","):
    states[int(state)] += 1

for days in range(256):
    new_states = defaultdict(int)
    for state, count in states.items():
        if state > 0:
            new_states[state - 1] += count
        else:
            new_states[6] += count
            new_states[8] += count
    states = new_states

print(sum(new_states.values()))
