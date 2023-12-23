from math import dist
X, Y, N, K = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(N)]

points.sort(key = lambda p: (dist((X,Y), p), p[0], p[1]))

for i in range(K):
    print(*points[i])