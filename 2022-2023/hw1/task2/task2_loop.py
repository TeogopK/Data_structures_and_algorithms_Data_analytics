# find all increasing subsequences, total_profit = sum(max - min)

# Note that there is a problem with the input:
# - example cases are 2 lines only: arr = list(map(int, input().split()))
# - real cases are N + 1 lines: arr = [int(input()) for _ in range(N)]

N = int(input())

arr = []

while True:
    try:
        arr.extend(map(int, input().split()))
    except Exception:
        break
        
total = 0

for i in range(len(arr) - 1):
    if arr[i] < arr[i + 1]:
        total += arr[i + 1] - arr[i]
        
print(total)