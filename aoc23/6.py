import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)
from math import sqrt

data = "6.txt"
# data = "6test.txt"
if len(sys.argv) > 1:
    data = f"6{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

##############################
# Part 1
##############################

time, dist = data.split("\n")
time = [int(x) for x in time.split()[1:]]
dist = [int(x) for x in dist.split()[1:]]

s = 1
for i in range(len(time)):
    T = time[i]
    D = dist[i]
    ok = 0
    for t in range(1, T):  # charge time
        d = t * (T - t)  # speed * time_remaining
        ok += d > D
    if ok:
        s *= ok

print(s)

##############################
# Part 2
##############################


T, D = data.split("\n")
T = int(T.replace(" ", "").split(":")[1])
D = int(D.replace(" ", "").split(":")[1])
# t such that t * (T - t) > D
# t * T - t^2 > D
# t^2 - t * T + D < 0
a = 1
b = -T
c = D
t1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
t2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
assert 0 < t1, t2 < T
# I assumed this was true as 0 and T are both impossible solutions although good sanity check
# below 0 - so between the two roots and t1 is the larger one
print(int(t1) - int(t2))


##############################
# Part 2 - brute force (12s)
##############################
ok = 0
for t in range(1, T):  # charge time
    ok += t * (T - t) > D
print(ok)
