def find_longest_unique(arr):
    max_length = 0
    s = set()
    left = 0

    for right in range(len(arr)):
        if arr[right] not in s:
            s.add(arr[right])
            max_length = max(max_length, right - left + 1)
        else:
            while arr[right] in s:
                s.remove(arr[left])
                left += 1
            s.add(arr[right])

    return max_length
    
Q = int(input())

for _ in range(Q):
    N = int(input())
    arr = list(map(int, input().split()))
    
    print(find_longest_unique(arr))
    