data = "data.txt"
# data = "datatest.txt"

with open(data) as f:
    data = f.read().strip()

res = 0 
res2 =0
p2 = True 
for i in range(len(data)):
    if (data[i:i+4]  == 'do()'):
        p2 = True
        continue
    if (data[i:i+7]  == 'don\'t()'):
        p2 = False
        continue
    if (data[i:i+4]!='mul('):
        continue
    j = i
    while (j < len(data) and data[j]!= ')'):
        j+=1
    if (j == len(data)):
        break
    try:
        x,y = list(map(int, data[i+4:j].split(',')))
    except:
        continue
    res += x * y 
    if (p2):
        res2+= x*y

print(res)
print(res2)

