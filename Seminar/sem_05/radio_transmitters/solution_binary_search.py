"""Solution not using the HackerRank input template"""
import bisect

def hackerlandRadioTransmitters(x, k):
    arr = sorted(set(x))
    total = 0
    
    i = 0
    
    while i < len(arr):
        index_best = bisect.bisect(arr, arr[i] + k)
        
        if index_best >= len(arr):
            total += 1
            break
        
        if arr[index_best] != arr[i] + k:
            index_best -= 1
        
        i = bisect.bisect(arr, arr[index_best] + k)
        total += 1
        
    return total

n, k = map(int, input().split())
x = [int(i) for i in input().split()]

answer = hackerlandRadioTransmitters(x, k)
print(answer)
