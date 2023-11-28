import sys
from collections import defaultdict, deque

DAY = 21
PART = 2

p1, p2 = [4, 8]
p1, p2 = [6, 1]


roll = 1
turn = 0
P1 = 0
P2 = 0


while True:
    if turn in [0, 1, 2]:
        p1 = (p1 + (roll - 1) % 100 + 1 - 1) % 10 + 1

    else:
        p2 = (p2 + (roll - 1) % 100 + 1 - 1) % 10 + 1

    if turn == 2:
        P1 += p1
    elif turn == 5:
        P2 += p2

    if P1 >= 1000:
        print(P1, P2, roll, P2 * roll)
        break
    if P2 >= 1000:
        print(P1, P2, roll, P1 * roll)
        break

    roll += 1
    turn = (turn + 1) % 6
