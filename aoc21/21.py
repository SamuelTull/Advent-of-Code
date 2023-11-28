import sys
from collections import defaultdict, deque
import heapq

DAY = 21
PART = 1

START = [4, 8]
START = [6, 1]


p1, p2 = START
P1 = P2 = 0
roll = 0
turn = 1


while True:
    if turn % 2 == 1:
        for _ in range(3):
            roll = roll % 100 + 1
            p1 += roll
        p1 = (p1 - 1) % 10 + 1
        P1 += p1
        if P1 >= 1000:
            print(P2 * turn * 3)
            break

    else:
        for _ in range(3):
            roll = roll % 100 + 1
            p2 += roll
        p2 = (p2 - 1) % 10 + 1
        P2 += p2
        if P2 >= 1000:
            print(P1 * turn * 3)
            break
    turn += 1


rolls = defaultdict(int)
for a in [1, 2, 3]:
    for b in [1, 2, 3]:
        for c in [1, 2, 3]:
            rolls[a + b + c] += 1

p1, p2 = START
states = {}
states[(0, 0, p1, p2)] = 1
Q = [(0, 0, p1, p2)]
wins = [0, 0]
goal = 21
while Q:
    P1, P2, p1, p2 = heapq.heappop(Q)
    state = states[(P1, P2, p1, p2)]
    # del states[(P1, P2, p1, p2)]
    # pop in order of P1/P2 wont ever get to this as cant add 0 or negative
    for roll, num in rolls.items():
        new_p1 = (p1 + roll - 1) % 10 + 1
        new_P1 = P1 + new_p1
        if new_P1 >= goal:
            wins[0] += num * state
        else:
            for roll2, num2 in rolls.items():
                new_p2 = (p2 + roll2 - 1) % 10 + 1
                new_P2 = P2 + new_p2
                if new_P2 >= goal:
                    wins[1] += num * num2 * state
                else:
                    if (new_P1, new_P2, new_p1, new_p2) in states:
                        states[(new_P1, new_P2, new_p1, new_p2)] += num * num2 * state
                    else:
                        heapq.heappush(Q, (new_P1, new_P2, new_p1, new_p2))
                        states[(new_P1, new_P2, new_p1, new_p2)] = num * num2 * state


print(max(wins))
