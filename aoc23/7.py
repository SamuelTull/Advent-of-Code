import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)


def rank_hand(hand, P2=False):
    value = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    counter = Counter(hand)
    values = [value[card] for card in hand]
    counts = sorted(counter.values(), reverse=True)

    if P2:
        value["J"] = 1
        values = [value[card] for card in hand]
        jokers = counter["J"]
        del counter["J"]
        counts = sorted(counter.values(), reverse=True)
        if counts:
            assert jokers < 5
            counts[0] += jokers
        else:
            assert jokers == 5
            counts = [5]

    ########################
    # Rankings
    ########################
    # 5 of a Kind
    if counts == [5]:
        return [9] + values
    # 4 of a Kind
    if counts == [4, 1]:
        return [8] + values
    # Full House
    if counts == [3, 2]:
        return [7] + values
    # 3 of a Kind
    if counts == [3, 1, 1]:
        return [4] + values
    # 2 Pairs
    if counts == [2, 2, 1]:
        return [3] + values
    # Pair
    if counts == [2, 1, 1, 1]:
        return [2] + values
    # High Card
    return [1] + values


data = "7.txt"
# data = "7test.txt"
if len(sys.argv) > 1:
    data = f"7{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

lines = [line.split() for line in data.split("\n")]

lines.sort(key=lambda line: rank_hand(line[0]))
s = 0
for i, line in enumerate(lines):
    s += (1 + i) * int(line[1])
print(s)

lines.sort(key=lambda line: rank_hand(line[0], True))
s = 0
for i, line in enumerate(lines):
    s += (1 + i) * int(line[1])
print(s)
