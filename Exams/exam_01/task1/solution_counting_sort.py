"""Counting sort"""

N = int(input())
arr = [int(i) for i in input().split()]

max_value = max(arr) + 1
counts = [0] * max_value

for el in arr:
    counts[el] += 1
    
for i in range(max_value):
    if counts[i] > 0:
        print(i, end = ' ')
