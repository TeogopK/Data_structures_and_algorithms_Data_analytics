"""Solution timeouts due to O(N^2) time complexity"""
N, D = map(int, input().split())
arr = [int(el) for el in input().split()]

count = 0
arr.sort()
    
for el in arr:
    if el + D in arr:
        count += 1
        
print(count)
