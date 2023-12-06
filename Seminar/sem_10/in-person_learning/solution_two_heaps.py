import heapq

N = int(input())
h = [tuple(map(int, input().split())) for _ in range(N)]

heapq.heapify(h)
answer = 0

current_rooms = []

while h:
    start, end = heapq.heappop(h)

    if start == end:
        continue
        
    while current_rooms and current_rooms[0] <= start:
        heapq.heappop(current_rooms)
        
    heapq.heappush(current_rooms, end)
    answer = max(answer, len(current_rooms))
    
print(answer)