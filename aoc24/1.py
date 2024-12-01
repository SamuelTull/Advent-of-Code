from collections import defaultdict
data = "1.txt"
with open(data) as f:
    data = f.read().strip()

groups = data.split("\n\n")
lines = data.split("\n")

res = res2 = 0
a = []
b = []
m = defaultdict(int)
for line in lines:
    line = line.split()
    x,y = line 
    a.append(int(x))
    b.append(int(y))
    m[int(y)] += 1

a.sort()
b.sort()

for i in range(len(a)):
    res += abs(a[i]-b[i])
    res2 += a[i]*m[a[i]]


print(res)
print(res2)
