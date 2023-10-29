# Solution using sort with lambda expression

N = int(input())
a = [int(input()) for i in range(N)]

a.sort(key = lambda x: x % 2 == 1)
print(*a, sep = '\n')