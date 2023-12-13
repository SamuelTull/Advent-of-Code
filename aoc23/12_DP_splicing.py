import sys


def solve(a, b):
    if a == "":
        return b == []

    key = (a, tuple(b))
    if key in cache:
        return cache[key]

    if a[0] == ".":
        ans = solve(a[1:], b)
    elif a[0] == "#":
        if not b:
            ans = 0
        else:
            b0 = b[0]
            if len(a) < b0 or "." in a[:b0]:
                ans = 0
            elif len(a) == b0:
                ans = solve(a[b0:], b[1:])
            else:
                # check next character after this block- it must be a "."
                char = a[b0]
                if char == "#":
                    ans = 0
                else:
                    ans = solve(a[b0 + 1 :], b[1:])
    else:
        ans = solve(a[1:], b) + solve("#" + a[1:], b)
    cache[key] = ans
    return ans


data = "12.txt"
# data = "12test.txt"
if len(sys.argv) > 1:
    data = f"12{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")
for P2 in [False, True]:
    s = 0
    for line in lines:
        a, b = line.split()
        b = list(map(int, b.split(",")))
        if P2:
            a = a + "?" + a + "?" + a + "?" + a + "?" + a
            b *= 5
        cache = {}
        s += solve(a, b)
    print(s)
