import sys
from collections import defaultdict, deque, Counter
import heapq
import functools  # @functools.lru_cache(maxsize=None)

remove = lambda string, chars="(),.=": "".join([x for x in string if x not in chars])

INF = 10 ** 32 

data = "data.txt"
# data = "test.txt"

with open(data) as f:
    data = f.read().strip()

lines = data.split("\n")


def max_dist(a):
    mx = 0
    for i in range(1,len(a)):
        mx = max(mx, abs(a[i]-a[i-1]))
    return mx   

def min_dist(a):
    mn = INF
    for i in range(1,len(a)):
        mn = min(mn, abs(a[i]-a[i-1]))
    return mn   

def safe(line):
    return (line == sorted(line) or line == sorted(line, reverse=True)) and max_dist(line) <=3 and min_dist(line)>0
    
def safe_i(line, i):
    line = [line[j] for j in range(len(line)) if i!=j]
    return (line == sorted(line) or line == sorted(line, reverse=True)) and max_dist(line) <=3 and min_dist(line)>0

res = 0
res2 = 0
for line in lines: 
    line = [int (x) for x in line.split()] # splits by blank space
    if safe(line):
        res+=1
        res2+=1
        continue
    for i in range(len(line)):
        if safe_i(line,i):
            res2+=1
            break
            
print(res)
print(res2)



