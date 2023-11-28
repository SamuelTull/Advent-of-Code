import numpy as np

"""data = open("in.txt").read()
# data = open("test.txt").read()
start, instr = data.split("\n\n")
start = [[x for x in line[1::4]] for line in start.split("\n")[:-1]]
col = np.array(start).T.tolist()
col = [[x for x in line[::-1] if x != " "] for line in col]



instr = [line.split(" ") for line in instr.split("\n")]
for line in instr:
    n, f, t = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
    for _ in range(n):
        rem = col[f].pop()
        col[t].append(rem)
s = ""
for c in col:
    s += c[-1]
print("P1",s)"""

############################

data = open("in.txt").read()
start, instr = data.split("\n\n")
start = [[x for x in line[1::4]] for line in start.split("\n")[:-1]]
instr = [line.split(" ") for line in instr.split("\n")]


for i in range(1, 3):
    col = [[x for x in line[::-1] if x != " "] for line in np.array(start).T]
    for line in instr:
        n, f, t = int(line[1]), int(line[3]) - 1, int(line[5]) - 1
        if i == 1:  # part 1
            for _ in range(n):
                rem = col[f].pop()
                col[t].append(rem)
        else:  # part 2
            rem = col[f][len(col[f]) - n :]
            col[f] = col[f][: len(col[f]) - n]
            col[t] += rem
    s = ""
    for c in col:
        s += c[-1]
    print(f"P{i}, {s}")
