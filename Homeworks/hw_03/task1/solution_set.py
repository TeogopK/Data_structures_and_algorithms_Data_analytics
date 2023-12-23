N, D = map(int, input().split())
arr = [int(el) for el in input().split()]
s = set(arr)

# Check if in fact there are only unique elements
if len(s) != len(arr):
    1 / 0

count = 0
arr.sort()

for el in arr:
    if el + D in s:
        count += 1
        
print(count)