from queue import PriorityQueue

G, T, groups_to_do, _ = map(int, input().split()) # K, T, B, N
arr = list(map(int, input().split()))[::-1]

waiting = PriorityQueue()

for _ in range(groups_to_do):
    
    i = 0
    while arr and i < T:
        waiting.put(arr.pop())
        i += 1
        
    i = 0
    while waiting and i < G:
        print(waiting.get(), end=' ')
        i += 1
        