def find(x, parents):
    if parents[x] == x:
        return x
    
    furthest_parent = find(parents[x], parents)
    parents[x] = furthest_parent

    return furthest_parent

def union(x, y, parents):
    x_root = find(x, parents)
    y_root = find(y, parents)
    
    parents[x_root] = y_root

def kruskal(V, edges):
    edges.sort(key=lambda x: (x[2], -x[3])) # profit must be maximum
    
    parents = [i for i in range(V + 1)]
    built_edges = []

    for x, y, cost, profit, index in edges:
        if find(x, parents) != find(y, parents):
            built_edges.append(index)
            union(x, y, parents)

    return built_edges

N, M = map(int, input().split())

edges = [list(map(int, input().split())) + [i] for i in range(1, M + 1)]

built_edges = kruskal(N, edges)
print(*built_edges, sep = '\n')