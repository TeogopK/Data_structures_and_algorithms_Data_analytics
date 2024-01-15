import sys
sys.setrecursionlimit(1_000_000)

def find(x, parents):
    if parents[x] == x:
        return x
    
    furthest_parent = find(parents[x], parents)
    parents[x] = furthest_parent

    return furthest_parent

def union(x, y, parents, rank):
    x_root = find(x, parents)
    y_root = find(y, parents)

    parents[x_root] = y_root

N, M = map(int, input().split())
edges = [map(int, input().split()) for _ in range(M)]
    
Q = int(input())
queries = (tuple(map(int, input().split())) for _ in range(Q))

def solve(V, edges, queries):
    rank = [0] * (V + 1)
    parents = [v for v in range(V + 1)]
    
    for x, y in edges:
        union(x, y, parents, rank)
        
    for x, y in queries:
        is_connected = find(x, parents) == find(y, parents)
        
        print(1 if is_connected else 0, end = ' ')

    
solve(N, edges, queries)

