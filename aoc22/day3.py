data = open("in.txt").read().strip()

"""
lines = [[x[: len(x) // 2], x[len(x) // 2 :]] for x in data.split("\n")]
p = [set(x for x in l[0]).intersection(set(x for x in l[1])).pop() for l in lines]
pp = [ord(p) - 96 if (p.upper() != p) else ord(p) - 64 + 26 for p in p]
print(sum(pp))"""

lines = [x for x in data.split("\n")]
x = 0
groups = []
N = len(lines)
while x <= len(lines) - 1:
    groups.append([lines[x], lines[x + 1], lines[x + 2]])
    x += 3

badge = [
    set(x for x in l[0])  # set(l[0]) ?!
    .intersection(set(x for x in l[1]))
    .intersection(set(x for x in l[2]))
    .pop()
    for l in groups
]
pp = [ord(p) - 96 if (p.upper() != p) else ord(p) - 64 + 26 for p in badge]
print(sum(pp))
