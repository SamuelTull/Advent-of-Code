data = {0: "in.txt", 1: "test.txt"}


data = open(data[0]).read().strip()
lines = data.split("\n")  # each line element of list
lines = [x.split(" ") for x in lines]
lines = list(map(lambda X: [X[0], int(X[1])], lines))

N = 10  # 2 for part 1
v = set()
pos = [[0, 0] for i in range(N)]
direction = {"R": (1, 0), "L": (-1, 0), "U": (0, -1), "D": (0, 1)}


for d, n in lines:
    d = direction[d]
    for _ in range(n):
        # move h
        pos[0][0] += d[0]
        pos[0][1] += d[1]
        for i in range(1, N):
            h = pos[i - 1]  
            t = pos[i]

            dx = h[0] - t[0]
            dy = h[1] - t[1]
            # dx = 0, 1, 2
            # dy = 0, 1, 2
            # (0,0), (0,1)/(1,0), (1,1)
            # (2,0)/(0,2) ... (2,1)/(1,2) ... (2,2)
            if dx == 2 or dx == -2:
                if dy == 0:
                    t[0] += dx / 2
                elif dy == 1 or dy == -1:
                    t[0] += dx / 2
                    t[1] += dy
                elif dy == 2 or dy == -2:
                    t[0] += dx / 2
                    t[1] += dy / 2

            elif dy == 2 or dy == -2:
                if dx == 0:
                    t[1] += dy / 2
                elif dx == 1 or dx == -1:
                    t[1] += dy / 2
                    t[0] += dx
        v.add(tuple(pos[-1]))
print(len(v))
