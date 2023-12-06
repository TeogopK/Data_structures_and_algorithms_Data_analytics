from queue import PriorityQueue

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

pq = PriorityQueue()
answer = 0

for start, end in sorted(arr):
    if start == end:
        continue
        
    while not pq.empty() and pq.queue[0] <= start:
        pq.get()
        
    pq.put(end)
    answer = max(answer, pq.qsize())
    
print(answer)