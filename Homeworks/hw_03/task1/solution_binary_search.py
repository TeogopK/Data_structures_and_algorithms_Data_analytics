def binary_search(arr, X):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if X < arr[mid]:
            right = mid - 1
        elif X > arr[mid]:
            left = mid + 1
        else:
            return True

    return False

N, D = map(int, input().split())
arr = [int(el) for el in input().split()]

count = 0
arr.sort()
    
for el in arr:
    if binary_search(arr, el + D):
        count += 1
        
print(count)
