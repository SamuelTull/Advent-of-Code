import sys
import ast

data_dict = {
    "in": "in.txt",
    "1": "in.txt",
    1: "in.txt",
    #
    "test": "test.txt",
    "0": "test.txt",
    0: "test.txt",
}

try:
    data = data_dict[sys.argv[1]]
except:
    data = data_dict[0]


with open(data) as f:
    data = f.read().strip()


groups = data.split("\n\n")
groups = [lines.split("\n") for lines in groups]
lines = []

for i in range(len(groups)):
    for j in range(len(groups[i])):
        groups[i][j] = ast.literal_eval(groups[i][j])
        lines.append(groups[i][j])


INT = type(0)
LST = type([])


def smaller(a, b):  # equal, bigger, smaller
    idx = 0
    a_ = b_ = True
    while True:

        if len(a) == idx:
            a_ = False
        if len(b) == idx:
            b_ = False

        if not a_ and not b_:
            return 0.5
        elif not a_ and b:
            return 0
        elif a_ and not b_:
            return 1

        if type(a[idx]) == INT == type(b[idx]):
            if a[idx] < b[idx]:
                return 0
            elif a[idx] > b[idx]:
                return 1
        elif type(a[idx]) == LST == type(b[idx]):
            Sab = smaller(a[idx], b[idx])
            if Sab != 0.5:
                return Sab
        elif type(a[idx]) == LST and type(b[idx]) == INT:
            Sab = smaller(a[idx], [b[idx]])
            if Sab != 0.5:
                return Sab
        elif type(a[idx]) == INT and type(b[idx]) == LST:
            Sab = smaller([a[idx]], b[idx])
            if Sab != 0.5:
                return Sab
        idx += 1


######################
###### P1
######################
correct = []
incorrect = []
equal = []
for i in range(len(groups)):
    S = smaller(groups[i][0], groups[i][1])
    if S == 0:
        correct.append(i + 1)
    elif S == 1:
        incorrect.append(i + 1)
    elif S == 0.5:
        equal.append(i + 1)
    else:
        print("Err", i)
print("P1", sum(correct))


######################
###### P2
######################
sorted_list = [[[2]], [[6]]]
while lines:
    new = lines.pop()
    idx = 0
    while True:
        if idx == len(sorted_list):
            sorted_list.append(new)
        if smaller(new, sorted_list[idx]) < 1:
            sorted_list.insert(idx, new)
            break
        else:
            idx += 1

P2 = 1
for i in range(len(sorted_list)):
    if sorted_list[i] == [[2]]:
        P2 *= i + 1
        # print("!!!!!!!!=", end=" ")
    elif sorted_list[i] == [[6]]:
        P2 *= i + 1
        # print("!!!!!!!!=", end=" ")

    # print(i + 1, ":", sorted_list[i])
print("P2:", P2)
