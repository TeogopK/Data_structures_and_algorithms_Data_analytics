def binary_search_leftmost(arr, X):
    left = 0
    right = len(arr) - 1

    Xi = 0

    while left <= right:
        mid = left + (right - left) // 2
        
        if X <= arr[mid]:
            right = mid - 1
            Xi = mid

        else:
            left = mid + 1

    return Xi

def binary_search_rightmost(arr, X):
    left = 0
    right = len(arr) - 1

    Xi = 0

    while left <= right:
        mid = left + (right - left) // 2

        if X < arr[mid]: # removes the = 
            right = mid - 1
        else:
            left = mid + 1
            Xi = mid # changes answer
    return Xi

N, Q = map(int, input().split())
arr = [int(el) for el in input().split()]

arr.sort()

for _ in range(Q):
    start, end = map(int, input().split())
    
    if start > end:
        print(0)
        continue
    
    count = binary_search_rightmost(arr, end) - binary_search_leftmost(arr, start) + 1
    print(count)