import sys
from collections import defaultdict

DAY = 18
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()


def find_close(s, i):
    assert s[i] == "("
    open_ = 1
    i += 1
    while True:
        if s[i] == "(":
            open_ += 1
        elif s[i] == ")":
            open_ -= 1
            if open_ == 0:
                return i
        i += 1


def parseBrackets(s):
    newS = []
    i = 0
    while i < len(s):
        if s[i] == "(":
            idx = find_close(s, i)
            newS.append(parseBrackets(s[i + 1 : idx]))
            i = idx + 1
        else:
            newS.append(s[i])
            i += 1
    return newS


def P1(s):
    if s[0] == "(":
        idx = find_close(s, 0)
        curr = P1(s[1:idx])
        i = idx + 1
    else:
        curr = int(s[0])
        i = 1
    while i < len(s):
        if s[i] == "*":
            if s[i + 1] == "(":
                idx = find_close(s, i + 1)
                curr *= P1(s[i + 2 : idx])
                i = idx + 1
            else:
                curr *= int(s[i + 1])
                i += 2
        elif s[i] == "+":
            if s[i + 1] == "(":
                idx = find_close(s, i + 1)
                curr += P1(s[i + 2 : idx])
                i = idx + 1
            else:
                curr += int(s[i + 1])
                i += 2
        else:
            assert False, f"{i}, {s[i]}\n{s}"
    return curr


def P2(s):
    newS = []
    if isinstance(s, str) or isinstance(s, int):
        return int(s)
    i = 0
    while i < len(s):
        if s[i] == "+":
            prev = newS.pop()
            newS.append(P2(prev) + P2(s[i + 1]))
            i += 2
        else:
            newS.append(s[i])
            i += 1
    curr = 1
    for i in range(0, len(newS), 2):
        curr *= P2(newS[i])
    return curr


p1 = p2 = 0
lines = data.split("\n")
for line in lines:
    line = line.replace("(", "( ").replace(")", " )").split(" ")
    p1 += P1(line)
    p2 += P2(parseBrackets(line))

print("P1:", p1)
print("P2:", p2)
