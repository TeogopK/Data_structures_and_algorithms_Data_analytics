import math
from queue import PriorityQueue
    
X, Y, N, K = map(int, input().split())
center = X, Y

pq = PriorityQueue() 

for _ in range(N):
    coordinates = tuple(map(int, input().split()))
    landmark = math.dist(center, coordinates), coordinates
    pq.put(landmark)

for _ in range(K):
    coordinates = pq.get()[1]
    print(*coordinates)