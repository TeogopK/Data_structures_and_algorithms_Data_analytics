N, M = map(int, input().split())
subseq = [int(input()) for _ in range(M)]

subseq.reverse() # use it as stack O(1) pop
subseq_set = set(subseq) # use it as a O(1) lookup

for num in range(1, N + 1):
    if num not in subseq_set:
        while subseq and num > subseq[-1]:
            print(subseq.pop(), end=' ')
        print(num, end=' ')
    
while subseq:
    print(subseq.pop(), end=' ')
    