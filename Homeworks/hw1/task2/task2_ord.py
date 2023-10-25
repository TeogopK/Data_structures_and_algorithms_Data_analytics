T = int(input())

for _ in range(T):
    n, k, str = input().split()
    k = int(k)
    
    for i in range(ord('A'), ord('Z') + 1):
        if str.count(chr(i)) >= k:
            print(chr(i), end = '')
            
    print()