from collections import deque

INF = -1

def bfs(starting_vertex, graph):
    q = deque([starting_vertex])
    visited = set([starting_vertex])

    distances = {v: INF for v in graph.keys()}
    distance = 0

    while q:
        for _ in range(len(q)):
            current = q.popleft()
            distances[current] = distance

            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        distance += 1

    return distances

K = int(input())
graph = {i: [] for i in range(300000)}

for _ in range(K):
    Xi, Yi = map(int, input().split())
    graph[Xi].append(Yi)
    graph[Yi].append(Xi)

distances = bfs(0, graph)

total_distance = sum(distances[node] for node in graph if distances[node] != INF)

print(total_distance)