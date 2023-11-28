import sys
from collections import defaultdict

DAY = 14
PART = 1

data = str(DAY)
if True:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

lines = data.split("\n")
M = {}
for line in lines:
    print(line)
    if line[:4] == "mask":
        mask = line.split(" ")[-1][::-1]
        print("newmask", mask)
        continue
    line = line.replace("[", " ").replace("]", " ").split(" ")
    ID = line[1]
    num = int(line[-1])

    for i, char in enumerate(mask):
        s = format(num, "b")
        if char == "0":
            num &= ~(1 << i)
        elif char == "1":
            num |= 1 << i
        else:
            assert char == "X", char
    # s = format(num, "b")
    M[ID] = num

print(M)
print(sum(x for x in M.values()))
