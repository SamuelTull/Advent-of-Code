import sys
from collections import defaultdict, deque
import heapq

DAY = 21
PART = 1

START = [4, 8]  # test
START = [6, 1]


def roll():
    global die
    die = die + 1
    return (die - 1) % 100 + 1


p1, p2 = START
P1 = P2 = 0
die = 0

while True:
    p1 += roll() + roll() + roll()
    P1 += (p1 - 1) % 10 + 1
    if P1 >= 1000:
        print(P2 * die)
        break
    p2 += roll() + roll() + roll()
    P2 += (p2 - 1) % 10 + 1
    if P2 >= 1000:
        print(P1 * die)
        break


rolls = defaultdict(int)
for a in [1, 2, 3]:
    for b in [1, 2, 3]:
        for c in [1, 2, 3]:
            rolls[a + b + c] += 1


import functools  # @functools.lru_cache(maxsize=None)


@functools.lru_cache(maxsize=None)
def solve(who, p1, p2, P1, P2):
    if P1 >= 21:
        return (1, 0)
    if P2 >= 21:
        return (0, 1)
    W1, W2 = (0, 0)
    for roll, num in rolls.items():
        if who == 0:
            new_p1 = (p1 + roll - 1) % 10 + 1
            new_P1 = P1 + new_p1
            w1, w2 = solve(1, new_p1, p2, new_P1, P2)
        else:
            new_p2 = (p2 + roll - 1) % 10 + 1
            new_P2 = P2 + new_p2
            (w1, w2) = solve(0, p1, new_p2, P1, new_P2)
        W1 += w1 * num
        W2 += w2 * num
    return (W1, W2)


p1, p2 = START
print(max(solve(0, p1, p2, 0, 0)))


@functools.lru_cache(maxsize=None)
def solve2(p1, p2, P1, P2):
    # p1 go now
    # if P1 >= 21:
    #     assert False
    if P2 >= 21:
        return (0, 1)
    W1, W2 = (0, 0)
    for roll, num in rolls.items():
        new_p1 = (p1 + roll - 1) % 10 + 1
        new_P1 = P1 + new_p1
        w2, w1 = solve2(p2, new_p1, P2, new_P1)
        W1 += w1 * num
        W2 += w2 * num
    return (W1, W2)


p1, p2 = START
print(max(solve2(p1, p2, 0, 0)))
