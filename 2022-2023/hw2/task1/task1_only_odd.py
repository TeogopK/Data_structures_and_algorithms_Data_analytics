# Solution storing only the odd values

N = int(input())
arr = []

for _ in range(N):
    a = int(input())
    
    if(a % 2 == 0):
        print(a)
    else:
        arr.append(a)

for el in arr:
    print(el)