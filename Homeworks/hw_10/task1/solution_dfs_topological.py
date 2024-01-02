from collections import defaultdict

def topological_dfs(current, stack, visited, graph):
    visited.add(current)
    
    for neighbor in graph[current]:
        if neighbor not in visited:
            visited.add(neighbor)
            topological_dfs(neighbor, stack, visited, graph)

    stack.append(current)

def topological_sort(graph):
    stack = []
    visited = set()

    for vertex in list(graph.keys()):
        if vertex in visited:
            continue
        topological_dfs(vertex, stack, visited, graph)

    stack.reverse()
    return stack

def create_graph(words):
    graph = defaultdict(set)
    
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

result = topological_sort(graph)

print(*result)