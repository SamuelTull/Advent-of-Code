data = {0: "in.txt", 1: "test.txt"}


data = open(data[0]).read().strip()
lines = data.split("\n")  # each line element of list
lines = [x.split(" ") for x in lines]
lines = list(map(lambda X: [X[0], int(X[1])], lines))

v = set()
h = [0, 0]
t = [0, 0]

direction = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}
for d, n in lines:
    d = direction[d]
    for i in range(n):
        # move h
        h[0] += d[0]
        h[1] += d[1]

        # move t
        dx = h[0] - t[0]
        dy = h[1] - t[1]
        # dx = 0, 1 , 2
        # dy = 0, 1, 1
        # (0,0), (0,1)/(1,0),
        # (2,0)/(0,2) ... (2,1)/(1,2)
        if dx == 2:
            if dy == 0:
                t[0] += 1
            elif dy == 1:
                t[0] += 1
                t[1] += 1
            elif dy == -1:
                t[0] += 1
                t[1] += -1
        elif dx == -2:
            if dy == 0:
                t[0] += -1
            elif dy == 1:
                t[0] += -1
                t[1] += 1
            elif dy == -1:
                t[0] += -1
                t[1] += -1

        elif dy == 2:
            if dx == 0:
                t[1] += 1
            elif dx == 1:
                t[1] += 1
                t[0] += 1
            elif dx == -1:
                t[1] += 1
                t[0] += -1
        elif dy == -2:
            if dx == 0:
                t[1] += -1
            elif dx == 1:
                t[1] += -1
                t[0] += 1
            elif dx == -1:
                t[1] += -1
                t[0] += -1

        v.add(tuple(t))
print(len(v))

print
