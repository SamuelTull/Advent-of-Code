import sys
import functools  # @functools.lru_cache(maxsize=None)


@functools.lru_cache(maxsize=None)
def solve(ai, bi, curr):
    # ai is current index in a
    # bi is current index in b
    # curr is current "#" streak
    if ai == len(a):
        if curr == 0 and bi == len(b):
            return 1
        if bi == len(b) - 1 and b[bi] == curr:
            return 1
        return 0
    ans = 0
    if a[ai] in ".?":
        if curr == 0:
            ans += solve(ai + 1, bi, 0)
        if bi < len(b) and b[bi] == curr:
            ans += solve(ai + 1, bi + 1, 0)
    if a[ai] in "?#":
        ans += solve(ai + 1, bi, curr + 1)
    return ans


data = "12.txt"
# data = "12test.txt"
if len(sys.argv) > 1:
    data = f"12{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()
lines = data.split("\n")
p1 = 0
p2 = 0
for i, line in enumerate(lines):
    a, b = line.split()
    b = list(map(int, b.split(",")))
    p1 += solve(0, 0, 0)
    solve.cache_clear()

    a, b = line.split()
    a = "?".join([a] * 5)
    b = ",".join([b] * 5)
    b = list(map(int, b.split(",")))
    p2 += solve(0, 0, 0)
    solve.cache_clear()
print(p1)
print(p2)
