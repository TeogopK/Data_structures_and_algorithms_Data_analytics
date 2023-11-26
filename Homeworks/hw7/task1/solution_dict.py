def find_longest_unique(arr):
    d = {}
    max_length = 0
    start = 0

    for index, num in enumerate(arr):
        if num in d:
            last_position = d[num]
            if last_position < start:
                pass
            else:
                max_length = max(max_length, index - start)
                start = last_position + 1
        d[num] = index

    return max(max_length, len(arr) - start)
    
Q = int(input())

for _ in range(Q):
    N = int(input())
    arr = list(map(int, input().split()))
    
    print(find_longest_unique(arr))