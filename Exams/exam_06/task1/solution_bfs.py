from collections import deque

def bfs(starting_vertex, num_traversal, parents, visited, graph):
    q = deque([starting_vertex])

    while q:
        current = q.popleft()
        parents[current] = num_traversal

        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)

                
def count_areas(V, graph):
    parents = [v for v in range(V + 1)]
    num_traversal = 0
    visited = set()

    for vertex in graph:
        if vertex in visited:
            continue
        bfs(vertex, num_traversal, parents, visited, graph)
        num_traversal += 1

    return parents

N, M = map(int, input().split())
graph = {v:set() for v in range(1, N + 1)}

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].add(y)
    graph[y].add(x)
    
Q = int(input())
queries = (tuple(map(int, input().split())) for _ in range(Q))

parents = count_areas(N, graph)

for x, y in queries:
    print(1 if parents[x] == parents[y] else 0, end = ' ')
