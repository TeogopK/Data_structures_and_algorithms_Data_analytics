import bisect

N, Q = map(int, input().split())
arr = [int(el) for el in input().split()]

arr.sort()

for _ in range(Q):
    start, end = map(int, input().split())
    
    if start > end:
        print(0)
        continue
    
    count = bisect.bisect_right(arr, end) - bisect.bisect_left(arr, start)
    print(count)
    