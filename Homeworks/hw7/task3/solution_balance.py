"""
Count the number of subarrays from the right of the median that have:
    - more bigger numbers than smaller compared to the median.
    - more smaller numbers than bigger.
    - equal number of smaller and bigger numbers than the median.

If you combine a right subarray with 1 more bigger number than smaller
with a subarray to the left of the median with 1 less bigger number than smaller,
you will get an array with the desired median.

The right subarray will be marked as balance +1, 
so every subarray to the left with balance -1
will give the desired median.
"""
from collections import defaultdict

N, B = map(int, input().split())
arr = list(map(int, input().split()))

index_B = arr.index(B)
d = defaultdict(int)

d[0] = 1 # number alone is an answer

balance = 0
for i in range(index_B + 1, N):
    balance += 1 if arr[i] > B else -1
    d[balance] += 1

total = d[0] # balanced only right subarrays are answers

balance = 0
for i in reversed(range(index_B)):
    balance += 1 if arr[i] > B else -1
        
    if -balance in d:
        total += d[-balance]
    
print(total)
