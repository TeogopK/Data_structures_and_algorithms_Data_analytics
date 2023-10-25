import functools

def comparator_concat(left, right):
    if left + right < right + left:
        return 1
    else:
        return -1

N = int(input())
arr = [input() for _ in range(N)]

if arr.count('0') == N:
    print(0)
    exit()

arr.sort(key=functools.cmp_to_key(comparator_concat))

print(*arr, sep='')
