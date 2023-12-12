import heapq

n = int(input())
pq = []
ranks = [int(x) for x in input().split()]

for rank in ranks:
    if rank == -1:
        if pq:
            print(pq[0], end=' ')
            heapq.heappop(pq)
        continue
    heapq.heappush(pq, rank)