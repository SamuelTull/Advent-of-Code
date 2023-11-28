import sys
from collections import defaultdict

DAY = 16
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

limitsdata, myticketdata, otherticketsdata = data.split("\n\n")
limits = {}
valid = set()
for line in limitsdata.split("\n"):
    line = line.replace(":", " or ").split(" or ")
    info = line[0].strip()
    l1, u1, l2, u2 = map(int, line[1].strip().split("-") + line[2].strip().split("-"))
    thisValid = set()
    for i in range(l1, u1 + 1):
        valid.add(i)
        thisValid.add(i)
    for i in range(l2, u2 + 1):
        valid.add(i)
        thisValid.add(i)
    limits[info] = thisValid

myticketdata = myticketdata.split("\n")[1]
mine = [int(x) for x in myticketdata.split(",")]
tickets = []

skipone = True
for line in otherticketsdata.split("\n"):
    if skipone:
        skipone = False
        continue
    tickets.append([int(x) for x in line.split(",")])


total = 0
invalid = []
for idx, ticket in enumerate(tickets):
    for x in ticket:
        if x not in valid:
            total += x
            if idx not in invalid:
                invalid.append(idx)
print("P1", total)


for idx in invalid[::-1]:
    tickets.pop(idx)


feasible = [[] for _ in range(len(mine))]
for idx in range(len(mine)):
    for classID, valid in limits.items():
        for ticket in tickets:
            if ticket[idx] not in valid:
                break
        else:
            feasible[idx].append(classID)

seen = set()
while len(seen) < len(mine):
    seen |= {x[0] for x in feasible if len(x) == 1}

    for i in range(len(feasible)):
        if len(feasible[i]) == 1:
            continue
        feasible[i] = [x for x in feasible[i] if x not in seen]

total = 1
for idx in range(len(feasible)):
    if "departure" in feasible[idx][0]:
        # print(feasible[idx], mine[idx])
        total *= mine[idx]

print("P2", total)
