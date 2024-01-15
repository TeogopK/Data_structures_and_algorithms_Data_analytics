def find(x, parents):
    if parents[x] == x:
        return x
    
    furthest_parent = find(parents[x], parents)
    parents[x] = furthest_parent

    return furthest_parent

def union(x, y, parents, rank):
    x_root = find(x, parents)
    y_root = find(y, parents)

    if rank[x_root] < rank[y_root]:
        parents[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parents[y_root] = x_root
    else:
        parents[x_root] = y_root
        rank[y_root] += 1

def are_connected(x, y, parents):
    return 1 if find(x, parents) == find(y, parents) else 0
        
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]


parents = [x for x in range(N + 1)]
rank = [0] * (N + 1)

for x, y in edges:
    union(x, y, parents, rank)

for query_type, x, y in queries:
    if query_type == 1:
        asnwer = are_connected(x, y, parents)
        print(asnwer, end = '')
    elif query_type == 2:
        union(x, y, parents, rank)

    