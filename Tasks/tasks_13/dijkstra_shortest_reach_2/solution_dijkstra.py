from heapq import heappop, heappush

def dijkstra(start, V, graph,):
    distances = [-1] * (V + 1)
    distances[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        total_weight, current = heappop(pq)
        
        for neighb, added_weight in graph[current]:
            new_weight = total_weight + added_weight
            
            if distances[neighb] == -1 or new_weight < distances[neighb]:
                distances[neighb] = new_weight
                heappush(pq, (new_weight, neighb))
    
    distances.remove(0)
    return distances[1::]
    
Q = int(input())

for _ in range(Q):
    N, M = map(int, input().split())
    graph = {v: set() for v in range(1, N + 1)}
    
    for _ in range(M):
        x, y, w = map(int, input().split())
        graph[x].add((y, w))
        graph[y].add((x, w))
    
    start = int(input())
    distances = dijkstra(start, N, graph)
    print(*distances)
