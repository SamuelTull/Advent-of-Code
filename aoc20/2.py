import sys
from collections import defaultdict

DAY = 2
PART = 1
data = str(DAY)
if len(sys.argv) > 1:
    if sys.argv[1] in ["0", "test"]:
        data = str(DAY) + "test"
    else:
        data = str(DAY) + sys.argv[1]

with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
C1 = 0
C2 = 0
for line in lines:
    I, password = line.split(":")
    nums, val = I.split(" ")
    l, r = nums.split("-")
    l, r = int(l), int(r)
    password = password.strip()
    s = sum(x == val for x in password)
    if l <= s <= r:
        C1 += 1

    password = " " + password
    N = 0
    if password[l] == val:
        N += 1
    if password[r] == val:
        N += 1
    if N == 1:
        C2 += 1

print(C1)
print(C2)
