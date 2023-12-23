import heapq
 
N = int(input())
 
arr = []
for _ in range(N):
    arr.append(tuple([int(x) for x in input().split()]))
 
arr.sort()    
 
pq = []
heapq.heapify(pq)
ans = 0
for s, e in arr:
    while len(pq) and pq[0] <= s:
        heapq.heappop(pq)
    
    if s < e:
        heapq.heappush(pq, e)
    ans = max(ans, len(pq))
    
print(ans)