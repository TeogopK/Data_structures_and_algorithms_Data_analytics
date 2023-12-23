from collections import defaultdict

N, R = map(int, input().split())
arr = map(int, input().split())

d = defaultdict(lambda: [0, 0])
count = 0

for el in arr:
    if el % R == 0:
        smaller = el // R
        count += d[smaller][1] # count of smaller as second number (and current as third)
        
        d[el][1] += d[smaller][0] # update count of current as second number
        
    d[el][0] += 1
    
print(count)