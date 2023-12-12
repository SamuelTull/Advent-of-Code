import sys
import functools  # @functools.lru_cache(maxsize=None)


@functools.lru_cache(maxsize=None)
def solve(ai, bi):
    # ai is current index in a
    # bi is current index in b
    if ai == len(a):
        if bi == len(b):
            return 1
        return 0
    ans = 0
    if a[ai] in ".?":
        ans += solve(ai + 1, bi)
    if a[ai] in "?#":
        if bi == len(b) or ai + b[bi] > len(a) or "." in a[ai : ai + b[bi]]:
            pass
        elif ai + b[bi] == len(a):
            ans += solve(ai + b[bi], bi + 1)
        elif a[ai + b[bi]] == "#":
            pass
        else:
            ans += solve(ai + b[bi] + 1, bi + 1)
    return ans


import time

data = "12.txt"
# data = "12test.txt"
if len(sys.argv) > 1:
    data = f"12{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()
lines = data.split("\n")
p1 = 0
p2 = 0
start = time.time()
for i, line in enumerate(lines):
    a, b = line.split()
    b = list(map(int, b.split(",")))
    p1 += solve(0, 0)
    solve.cache_clear()

    a, b = line.split()
    a = "?".join([a] * 5)
    b = ",".join([b] * 5)
    b = list(map(int, b.split(",")))
    p2 += solve(0, 0)
    solve.cache_clear()
print(p1)
print(p2)
print(time.time() - start)
