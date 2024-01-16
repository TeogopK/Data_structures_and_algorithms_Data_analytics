from heapq import heappop, heappush

INF = float('infinity')
DIVIDER = 10**9 + 7

def dijkstra(start, end, V, graph):
    distances = [INF] * (V + 1)
    distances[start] = 0
    
    ways_to_get_there = [0] * (V + 1)
    ways_to_get_there[start] = 1

    visited = set()
    
    pq = [(0, start)]
    
    while pq:
        total_weight, current = heappop(pq)
        
        if current in visited:
            continue
        visited.add(current)
        
        for neighb, added_weight in graph[current]:
            if neighb in visited:
                continue
                
            new_weight = total_weight + added_weight
            
            if distances[neighb] == INF or new_weight < distances[neighb]:
                distances[neighb] = new_weight
                heappush(pq, (new_weight, neighb))
                ways_to_get_there[neighb] = ways_to_get_there[current]
            elif new_weight == distances[neighb]:
                ways_to_get_there[neighb] += ways_to_get_there[current]
                ways_to_get_there[neighb] %= DIVIDER
       
    return distances[end], ways_to_get_there[end]

N, M = map(int, input().split())
graph = {v: [] for v in range(1, N + 1)}

for _ in range(M):
    x, y, w = map(int, input().split())
    w %= DIVIDER

    graph[x].append((y,w))

start = 1
end = N

minimum_dist, paths = dijkstra(start, end, N, graph)
minimum_dist = -1 if minimum_dist == INF else minimum_dist

print(minimum_dist, paths)
