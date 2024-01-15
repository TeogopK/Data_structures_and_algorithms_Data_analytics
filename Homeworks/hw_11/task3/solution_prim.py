from heapq import heappush, heappop

def prim(start, V, graph):
    visited = set()
    pq = [(0, 0, 0, start)]
    built_edges = []
    
    while len(visited) != V:
        _, _, edge_index, current_vertex = heappop(pq)
        
        if current_vertex in visited:
            continue
        
        visited.add(current_vertex)
        built_edges.append(edge_index)
        
        for neighb, weight, profit, index in graph[current_vertex]:
            if neighb in visited:
                continue
                            
            heappush(pq, (weight, profit, index, neighb))
    
    return built_edges[1:]

N, M = map(int, input().split())
graph = {v: set() for v in range(1, N + 1)}

for index in range(1, M + 1):
    x, y, cost, profit = map(int, input().split())
    graph[x].add((y, cost, -profit, index))
    graph[y].add((x, cost, -profit, index))

built_edges = prim(1, N, graph)
print(*built_edges, sep = '\n')