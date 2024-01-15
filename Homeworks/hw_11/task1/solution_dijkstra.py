from heapq import heappop, heappush
from math import ceil

INF = -1

def dijkstra(start, end, V, intervals, graph):
    distances = [INF] * V
    distances[start] = 0

    visited = set()
    
    pq = [(0, start)]
    
    while pq:
        total_weight, current = heappop(pq)
        
        if current == end:
            break
        
        if current in visited:
            continue
        visited.add(current)
        
        total_weight = ceil(total_weight / intervals[current]) * intervals[current]
        
        for neighb, added_weight in graph[current]:
            if neighb in visited:
                continue
                
            new_weight = total_weight + added_weight
            
            if distances[neighb] == INF or new_weight < distances[neighb]:
                distances[neighb] = new_weight
                heappush(pq, (new_weight, neighb))
    
    return distances[end]

V, E, start, end = map(int, input().split())
intervals = [int(input()) for _ in range(V)]

graph = {v: set() for v in range(V)}
for _ in range(E):
    x, y, w = map(int, input().split())
    graph[x].add((y,w))
    
total_time = dijkstra(start, end, V, intervals, graph)
print(total_time)