N = int(input())
K = int(input())

arr = [int(input()) for _ in range(N)]
arr.sort()

min = arr[-1]

for i in range(0, len(arr) - K + 1):
    diff = arr[i + K - 1] - arr[i]
    
    if min > diff:
        min = diff
        
print(min)