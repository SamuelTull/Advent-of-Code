import sys
from collections import defaultdict, deque, Counter

DAY = 14
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

line = data.split("\n\n")[0].strip()
counts = defaultdict(int)
for i in range(len(line) - 1):
    counts[line[i : i + 2]] += 1

pairs = {}
for pair in data.split("\n\n")[1].split("\n"):
    a, b = pair.split(" -> ")
    pairs[a] = b

for repeat in range(40):
    new_counts = defaultdict(int)
    for (a, b), count in counts.items():
        if a + b in pairs:
            c = pairs[a + b]
            new_counts[a + c] += count
            new_counts[c + b] += count
        else:
            new_counts[a + b] += count
    counts = new_counts

p = defaultdict(int)
for (a, b), count in counts.items():
    p[a] += count / 2
    p[b] += count / 2
p[line[0]] += 1 / 2
p[line[-1]] += 1 / 2


p = sorted(p.values())
print(p[-1] - p[0])
