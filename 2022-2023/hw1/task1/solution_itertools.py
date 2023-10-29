from itertools import groupby

for _ in range(int(input())):
    length, arr = input().split()
    
    print(int(length) - len(list(groupby(arr))))