from collections import deque

def walk_flaming_trees(i, j):
    q.append((i, j))
    
    length = [i, i]
    width = [j, j]

    while q:
        x, y = q.popleft()

        if visited[x][y]:
            continue

        visited[x][y] = True

        if x-1 >= 0 and not visited[x-1][y] and inflames[x-1][y]:
            q.append((x-1, y))
            length[0] = min(x-1, length[0])

        if x+1 < N and not visited[x+1][y] and inflames[x+1][y]:
            q.append((x+1, y))
            length[1] = max(x+1, length[1])

        if y-1 >= 0 and not visited[x][y-1] and inflames[x][y-1]:
            q.append((x, y-1))
            width[0] = min(y-1, width[0])

        if y+1 < N and not visited[x][y+1] and inflames[x][y+1]:
            q.append((x, y+1))
            width[1] = max(y+1, width[1])

    w = width[1] - width[0] + 1
    l = length[1] - length[0] + 1 
    
    return w*l


N = int(input())
inflames = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

areas = []
q = deque()

for i in range(N):
    for j in range(N):
        if visited[i][j] or not inflames[i][j]:
            continue
            
        area = walk_flaming_trees(i, j)
        areas.append(area)
        
areas.sort(reverse=True)
print(*areas)
                