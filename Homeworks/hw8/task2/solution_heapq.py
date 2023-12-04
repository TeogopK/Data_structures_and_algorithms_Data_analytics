import heapq

G, T, groups_to_do, _ = map(int, input().split()) # K, T, B, N
arr = list(map(int, input().split()))[::-1]

waiting = []

for _ in range(groups_to_do):
    
    i = 0
    while arr and i < T:
        heapq.heappush(waiting, arr.pop())
        i += 1
        
    i = 0
    while waiting and i < G:
        print(heapq.heappop(waiting), end=' ')
        i += 1
        