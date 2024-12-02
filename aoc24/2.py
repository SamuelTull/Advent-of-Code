
data = "data.txt"
# data = "datatest.txt"

with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")

def safe(line):
    if not (line == sorted(line) or line == sorted(line, reverse=True)):
        return False
    for i in range(1, len(line)):
        d = abs(line[i] - line[i-1])
        if not (1<=d<=3):
            return False
    return True

def safe2(line):
    for j in range(len(line)):
        if safe([line[i] for i in range(len(line)) if i!=j]):
            return True
    return False    

res = 0
res2 = 0
for line in lines: 
    line = [int (x) for x in line.split()] # splits by blank space
    if safe(line):
        res+=1
        res2+=1
    elif safe2(line):
        res2+=1
    
            
print(res)
print(res2)



