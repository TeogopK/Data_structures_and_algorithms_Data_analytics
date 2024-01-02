from collections import deque

def topological_bfs(graph):
    in_degree = {v: 0 for v in graph.keys()}

    for vertex in graph.keys():
        for child in graph[vertex]:
            in_degree[child] += 1

    stack = [v for v in graph.keys() if in_degree[v] == 0]
    
    q = deque(stack)
    visited = set(stack)

    while q:
        current = q.popleft()

        for neighbor in graph[current]:
            if neighbor not in visited:
                in_degree[neighbor] -= 1
            
            if in_degree[neighbor] == 0:
                visited.add(neighbor)
                q.append(neighbor)
                stack.append(neighbor)

    return stack

def create_graph(words):
    unique_characters = set(ch for word in words for ch in word)
    graph = {v: set() for v in unique_characters}
    
    for i in range(N - 1):
        j = 0

        max_size = min(len(words[i]), len(words[i+1]))

        while j < max_size and words[i][j] == words[i+1][j]:
            j += 1

        if j < max_size:
            first, second = words[i][j], words[i+1][j]
            graph[first].add(second)
            
    return graph


N = int(input())

words = [input() for _ in range(N)]
graph = create_graph(words)

result = topological_bfs(graph)

print(*result)