"""Note that the graph is unweighted so BFS is faster"""
from heapq import heappop, heappush

INF = float('infinity')

def dijkstra(start, V, graph):
    distances = [INF] * V
    distances[start] = 0

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
    
    return distances

K = int(input())
graph = {i: [] for i in range(300000)}

for _ in range(K):
    Xi, Yi = map(int, input().split())
    graph[Xi].append((Yi, 1))
    graph[Yi].append((Xi, 1))

distances = dijkstra(0, len(graph), graph)

total_distance = sum(distances[node] for node in graph if distances[node] != INF)

print(total_distance)