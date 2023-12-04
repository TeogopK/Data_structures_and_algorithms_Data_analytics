import heapq

def solve_query():
    N, C = map(int, input().split())
    
    groups = [tuple(map(int, input().split())) for _ in range(N)]
    groups = [(X, Y, K) for K, X, Y in groups]
    heapq.heapify(groups)
    
    current = []
    total = 0
    
    while groups:
        X, Y, K = heapq.heappop(groups)
        
        while current and current[0][0] <= X:
            _, _, freed = heapq.heappop(current)
            total -= freed
        
        if X >= Y: # Not used but good practice
            continue
            
        heapq.heappush(current, (Y, X, K))
            
        total += K
        if total > C:
            return 0
        
    return 1


Q = int(input())
for _ in range(Q):
    print(solve_query())
        