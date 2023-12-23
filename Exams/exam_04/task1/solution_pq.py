from queue import PriorityQueue

N = int(input())
tasks = list(map(int, input().split()))

commandos = PriorityQueue()

for t in tasks:
    if t == -1 and not commandos.empty():
        print(commandos.get_nowait(), end=' ')
    if t != -1:
        commandos.put_nowait(t)
        