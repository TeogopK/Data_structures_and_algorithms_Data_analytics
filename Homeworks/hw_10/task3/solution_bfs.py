from collections import defaultdict, deque

def bfs(start):
    q = deque([start])

    visited = [False for _ in range(N + 1)]
    visited[start] = True
    distance = 0

    while q:
        length = len(q)

        for _ in range(length):
            current = q.popleft()

            if friend_groups[current] == F:
                return distance

            for child in graph[current]:
                if not visited[child]:
                    q.append(child)
                    visited[current] = True

        distance += 1    
    
    return -1


N, M = map(int, input().split())
graph = defaultdict(lambda: [])

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
friend_groups = [-1] + list(map(int, input().split())) # starts at index 1
F = friend_groups[-1]

start = friend_groups.index(F)
friend_groups[start] = -1
    
print(bfs(start))
