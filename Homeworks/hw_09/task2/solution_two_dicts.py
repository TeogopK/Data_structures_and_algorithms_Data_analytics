from collections import defaultdict

N, M = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]

ans = 0

d1 = defaultdict(int)
d2 = defaultdict(int)

for i, num in enumerate(arr):
    if i > 1:
        ans += d2[num / M]
    if i > 0:
        d2[num] += d1[num / M]
    d1[num] += 1
    
print(ans)