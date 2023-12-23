import string

T = int(input())

for _ in range(T):
    _, k, str = input().split()
    k = int(k)
    
    for ch in string.ascii_uppercase:
        if str.count(ch) >= k:
            print(ch, end = '')
           
    print()