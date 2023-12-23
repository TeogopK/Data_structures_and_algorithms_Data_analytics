"""Solution using our own sort function"""

def comparator_concat(left, right):
    return left + right >= right + left
    
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2

        left_arr = arr[:middle]
        right_arr = arr[middle:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        merge(arr, left_arr, right_arr)
        
def merge(arr, left_arr, right_arr):
    index = left = right = 0
    left_size = len(left_arr)
    right_size = len(right_arr)

    while left < left_size and right < right_size:
        if comparator_concat(left_arr[left], right_arr[right]):
            arr[index] = left_arr[left] 
            left += 1
        else:
            arr[index] = right_arr[right] 
            right += 1
        index += 1

    while left < left_size:
        arr[index] = left_arr[left]
        index += 1
        left += 1

    while right < right_size:
        arr[index] = right_arr[right]
        index += 1
        right += 1

N = int(input())
arr = [input() for _ in range(N)]

if arr.count('0') == N:
    print(0)
    exit()

merge_sort(arr)

print(*arr, sep='')
