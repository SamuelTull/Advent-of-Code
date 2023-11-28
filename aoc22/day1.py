data = open("in.txt").read().strip()

p = [x for x in data.split("\n\n")]
psum = [sum(int(x) for x in x.split("\n")) for x in p]
psum.sort()
print(psum[-1])
print(sum(psum[-3:]))
