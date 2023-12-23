N = int(input())

arr = [(*map(int, input().split()), i + 1) for i in range(N)]

# Using tuple for multiple criteria
arr.sort(key = lambda x: (x[0] ** 2/ x[1], x[0]), reverse = True)

res = [el[2] for el in arr]

print(*res)