import sys
from collections import defaultdict

DAY = 10
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = [int(x) for x in data.split("\n")]

lines = sorted(lines)
lines.append(max(lines) + 3)
lines = [0] + lines
diff = [0] * 4
for i in range(1, len(lines)):
    d = lines[i] - lines[i - 1]
    diff[d] += 1
print("P1", diff[1] * diff[3])

# keeping list of valid connections got too big
# realised I only needed to keep track of last one
# used dicts

lines = [int(x) for x in data.split("\n")]
lines.append(max(lines) + 3)
lines.append(0)
lines.sort()
valid = {x: 0 for x in lines}
valid[lines[0]] = 1
for i in range(1, len(lines)):
    for j in range(i):
        if lines[i] - lines[j] <= 3:
            valid[lines[i]] += valid[lines[j]]
        else:
            valid[lines[j]] = 0
print("P2", valid[lines[-1]])

for v in valid:
    print(v, valid[v])

lines = [int(x) for x in data.split("\n")]
lines.append(max(lines) + 3)
lines.append(0)
lines.sort()

memo = {}


def dp(i):
    if i == len(lines) - 1:
        return 1
    if i in memo:
        return memo[i]
    ans = 0
    for j in range(i + 1, len(lines)):
        if lines[j] - lines[i] <= 3:
            ans += dp(j)
    memo[i] = ans
    return ans


print("P2-DP", dp(0))

for v in memo:
    print(v, lines[v], memo[v])
