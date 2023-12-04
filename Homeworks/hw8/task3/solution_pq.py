from queue import PriorityQueue

def solve_query():
    N, C = map(int, input().split())
    
    groups = PriorityQueue() 
    for _ in range(N):
        K, X, Y = map(int, input().split())
        groups.put((X, Y, K))
    
    current = PriorityQueue() 
    total = 0
    
    while not groups.empty():
        X, Y, K = groups.get()
        
        while not current.empty() and current.queue[0][0] <= X:
            _, _, freed = current.get()
            total -= freed
        
        if X >= Y: # Not used but good practice
            continue
            
        current.put((Y, X, K))
            
        total += K
        if total > C:
            return 0
        
    return 1


Q = int(input())
for _ in range(Q):
    print(solve_query())
        