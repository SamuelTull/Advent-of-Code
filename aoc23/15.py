import sys

data = "15.txt"
# data = "15test.txt"
if len(sys.argv) > 1:
    data = f"15{sys.argv[1]}.txt"
with open(data) as f:
    data = f.read().strip()

groups = data.split(",")


def hash(s):
    ans = 0
    for c in s:
        ans = (ans + ord(c)) * 17 % 256
    return ans


ans = 0
for group in groups:
    ans += hash(group)
print(ans)

boxes = [[] for _ in range(256)]
for group in groups:
    if "=" in group:
        (s, v) = group.split("=")
        bi = hash(s)
        for box in boxes[bi]:
            if box[0] == s:
                box[1] = v
                break
        else:
            boxes[bi].append([s, v])
    else:
        (s, v) = group.split("-")
        bi = hash(s)
        for i, box in enumerate(boxes[bi]):
            if box[0] == s:
                boxes[bi].pop(i)
                break

ans = 0
for i, box in enumerate(boxes):
    for j, (s, v) in enumerate(box):
        ans += (i + 1) * (j + 1) * int(v)
print(ans)
