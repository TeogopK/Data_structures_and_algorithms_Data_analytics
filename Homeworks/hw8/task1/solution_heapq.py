import math
import heapq
    
X, Y, N, K = map(int, input().split())
center = X, Y

pq = []

for _ in range(N):
    coordinates = tuple(map(int, input().split()))
    landmark = math.dist(center, coordinates), coordinates
    heapq.heappush(pq, landmark)

for _ in range(K):
    coordinates = heapq.heappop(pq)[1]
    print(*coordinates)