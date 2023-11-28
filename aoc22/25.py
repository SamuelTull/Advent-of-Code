import sys
from collections import defaultdict, deque

DAY = 25
PART = 1

data = str(DAY)
if True:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()


def baseToNumber(s):
    total = 0
    for i, x in enumerate(s[::-1]):
        if x == "-":
            x = -1
        elif x == "=":
            x = -2
        else:
            x = int(x)
        total += x * (5**i)
    return total


def numberToBase(n):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(n % 5)
        n //= 5
    digits.append(0)
    digits = digits[::-1]

    for i in range(len(digits) - 1, -1, -1):
        if digits[i] in [3, 4, 5]:
            digits[i - 1] += 1
        digits[i] = {5: "0", 4: "-", 3: "=", 2: "2", 1: "1", 0: "0"}[digits[i]]
    return "".join(digits)


lines = data.splitlines()
total = 0
for line in lines:
    total += baseToNumber(line)


print("Total=", total)
print(numberToBase(total))
