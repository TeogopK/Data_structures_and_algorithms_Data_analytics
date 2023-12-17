N = int(input())
arr = list(map(int, input().split()))

d = {}
minimal = N

for i, el in enumerate(arr):
    if el in d:
        minimal = min(minimal, i - d[el])
    d[el] = i
    
print(minimal)
        