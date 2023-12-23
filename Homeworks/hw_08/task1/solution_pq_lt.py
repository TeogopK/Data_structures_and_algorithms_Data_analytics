import math
from queue import PriorityQueue

class Landmark():
    def __init__(self, X, Y, base_coordinates):
        self.coordinates = X, Y
        self.distance = math.dist(self.coordinates, base_coordinates)
        
    def __lt__(self, other):
        if self.distance == other.distance:
            return self.coordinates < other.coordinates
        return self.distance < other.distance
    
X, Y, N, K = map(int, input().split())
base_coordinates = X, Y

pq = PriorityQueue() 

for _ in range(N):
    Xi, Yi = map(int, input().split())
    landmark = Landmark(Xi, Yi, base_coordinates)
    pq.put(landmark)

for _ in range(K):
    landmark = pq.get()
    print(*landmark.coordinates)