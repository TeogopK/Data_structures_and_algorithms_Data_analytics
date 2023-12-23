N = int(input())

arr = list(map(int, input().split()))
sorted_arr = sorted(arr)

first = 0
last = N - 1

while first < N and arr[first] == sorted_arr[first]:
    first += 1
   
while last >= 0 and arr[last] == sorted_arr[last]:
    last -= 1

res = last - first + 1

if first > last: # when input is sorted
    res = 0
    
print(res)