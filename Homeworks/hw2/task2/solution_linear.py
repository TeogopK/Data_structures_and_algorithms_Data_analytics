""" Test cases:
1
1 2 3 4 
1 2 3 3 3
1 3 2 4 5 6 8 7 9
1 3 2 4 5 6 10 7 8 9
1 3 2 5 -1 100 10 7 8 9

2 3 4 5 6 1  -->  6
-2 -1 0 2 3 4 5 6 1 --> 6
-2 -1 0 2 4 3 5 6 1 --> 6
-2 -1 0 2 4 3 9 6 1 7 8 --> 8
"""

def find_shortest_unsorted_subarray(N, arr):
    """
    1. Find the first swap.
    2. Find the last swap.
        Note the area between first swap and last swap may not be the full answer.
    
    3. Find the minimum element in the "left" area - between first swap and last swap.
    4. Find where the minimum elent should be placed in the "first" area - between 0 and first swap.
        This is the beginning of the searched subarray.
    
    5. Repeat 3. and 4. for maximum element.
        This is gonna find the end of the searched subarray.
        
    The number of elements in it is (end - start + 1)
    """
    
    if N <= 1: # trivial cases
        return 0
    
    first = 0
    last = N - 1

    while first < N - 1 and arr[first] <= arr[first + 1]:
        first += 1

    while last > 0 and arr[last] >= arr[last - 1]:
        last -= 1

    if first > last: # when input is sorted
        return 0
    
    min_misplaced = min(arr[first : last + 1])
    max_misplaced = max(arr[first : last + 1])
    
    for i in range(first):
        if arr[i] > min_misplaced:
            first = i
            break
            
    for i in range(N - 1, last, -1):
        if arr[i] < max_misplaced:
            last = i
            break
            
    return last - first + 1 
    
N = int(input())
arr = list(map(int, input().split()))
    
res = find_shortest_unsorted_subarray(N, arr)
print(res)
