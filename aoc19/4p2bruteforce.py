import sys
from collections import defaultdict, deque

DAY = 4
PART = 2


def ascending(p):
    p = str(p)
    for i in range(1, len(p)):
        if p[i] < p[i - 1]:
            return False
    return True


def double(p):
    p = str(p)
    for i in range(len(p) - 1):
        if p[i] == p[i + 1]:
            return True
    return False


def p2(p):
    p = str(p)
    i = 0
    if p[i] == p[i + 1] != p[i + 2]:
        return True
    i = 4
    if p[i] == p[i + 1] != p[i - 1]:
        return True
    for i in range(1, 4):
        if p[i - 1] != p[i] == p[i + 1] != p[i + 2]:
            return True
    return False


m = 136760
M = 595730
P1 = P2 = 0
s1 = set()
for p in range(m, M + 1):
    if ascending(p):
        if double(p):
            P1 += 1
        if p2(p):
            P2 += 1
print("P1", P1, "P2", P2)
