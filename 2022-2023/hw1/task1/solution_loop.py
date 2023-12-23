q = input()

for _ in range(int(q)):
    length, arr = input().split()
    
    count = 0
    for i in range(1, int(length)):
        if arr[i] == arr[i - 1]:
            count += 1
            
    print(count)
    