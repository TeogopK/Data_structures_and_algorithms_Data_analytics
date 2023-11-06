def binary_search(arr, X):
    l = 0
    r = len(arr) - 1
    
    indx, checks = -1, 0
    
    while l <= r:
        checks += 1
        mid = (l + r) // 2
        
        if X < arr[mid]:
            r = mid - 1
        elif X > arr[mid]:
            l = mid + 1
        else:
            indx = mid
            return indx, checks
            
    return indx, checks

N = int(input())
arr = [int(i) for i in input().split()]

K = int(input())
queries = [int(i) for i in input().split()]

index_arr = []
checks_arr = []

for q in queries:
    indx, checks = binary_search(arr, q)
    
    index_arr.append(indx)
    checks_arr.append(checks)

print(*index_arr)
print(*checks_arr)