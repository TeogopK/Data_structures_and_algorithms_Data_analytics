import heapq

N, Q = [int(x) for x in input().split()]

intervals = [int(x) for x in input().split()]
intervals = [(intervals[2 * i], intervals[2 * i + 1]) for i in range(len(intervals) // 2)]
queries = [(int(x), i) for i, x in enumerate(input().split())]

intervals.sort(reverse=True)
sorted_queries = sorted(queries)

ans = [-1 for _ in range(len(queries))]
pq = []

for query in sorted_queries:
    while len(pq) and pq[0] < query[0]:
        heapq.heappop(pq)
    
    while len(intervals) and intervals[-1][0] <= query[0]:
        if intervals[-1][1] >= query[0]:
            heapq.heappush(pq, intervals[-1][1])
        intervals.pop()
        
    ans[query[1]] = len(pq)
    
for count_ in ans:
    print(count_, end=' ')