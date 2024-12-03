data= "data.txt"
# data = "datatest.txt"

with open(data) as f:
    s = f.read().strip()


res = 0;
res2 = 0; 

for c in "YN[]":
    s = s.replace(c, " ")

s = s.replace("do()", " Y ")
s = s.replace("don't()", " N ")
s = s.replace(")", "] ")  
s = s.replace("mul(", " [")  


blocks = s.split()
p2 = True
for b in blocks:
    if (b == 'Y'): 
        p2 = True
    if (b == 'N'):
        p2 = False
    if (b[0]!='[' or b[-1]!=']'):
        continue
    try:
        x,y = list(map(int, b[1:-1].split(',')))
    except:
        continue
    res += x * y
    if (p2):
        res2 +=  x * y
    
print(res)
print(res2)


