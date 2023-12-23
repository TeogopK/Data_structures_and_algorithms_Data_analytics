N = int(input())

arr = [(*map(int, input().split()), i + 1) for i in range(N)]

arr.sort(key = lambda x: x[0], reverse = True) # first sort by diameter
arr.sort(key = lambda x: x[0] ** 2 / x[1], reverse = True) # sorting is stable

res = [el[2] for el in arr]

print(*res)