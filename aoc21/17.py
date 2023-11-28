import sys
from collections import defaultdict, deque

DAY = 17
PART = 1

data = str(DAY)
if False:  # change for test data debugging
    data = str(DAY) + "test"
if len(sys.argv) > 1:
    data = str(DAY) + sys.argv[1]
with open(data + ".txt") as f:
    data = f.read().strip()

line = data.strip()
print(line)
line = line.replace(",", "").replace("=", " ").replace("..", " ")
_, _, _, x1, x2, _, y1, y2 = line.split()
x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
x1, x2 = min(x1, x2), max(x1, x2)
y1, y2 = min(y1, y2), max(y1, y2)
print(x1, x2, y1, y2)
assert x1 > 0  # xv has to be positive
# for part 1 yv is clearly positive
# wanted to do a clever method to see if yv is already too high
# but brute force is fast enough


p1 = 0
p2 = 0
for XV in range(1, 1000):
    for YV in range(-1000, 1000):
        this = [XV, YV]
        xv, yv = XV, YV
        x, y = 0, 0
        maxy = 0
        while y > y1 and x < x2:
            x += xv
            y += yv
            xv -= 1 if xv > 0 else (-1 if xv < 0 else 0)
            yv -= 1
            if y > maxy:
                maxy = y
            if x1 <= x <= x2 and y1 <= y <= y2:
                p2 += 1
                if maxy >= p1:
                    p1 = maxy
                break
print(p1)
print(p2)
