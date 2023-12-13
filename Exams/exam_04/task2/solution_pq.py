from queue import PriorityQueue

N, Q = map(int, input().split())

intervals_arr = list(map(int, input().split()))
intervals = PriorityQueue()

for i in range(0, len(intervals_arr), 2):
    intervals.put((intervals_arr[i], intervals_arr[i+1]))

queries = [(int(num), i) for i, num in enumerate(input().split())]
queries.sort()

current = PriorityQueue()
results = [0] * Q

for time, index in queries:  
    while not current.empty() and current.queue[0] < time:
        current.get()
        
    while not intervals.empty() and intervals.queue[0][0] <= time:
        start, end = intervals.get()
        if end >= time:
            current.put(end)

    results[index] = current.qsize()
        
print(*results)