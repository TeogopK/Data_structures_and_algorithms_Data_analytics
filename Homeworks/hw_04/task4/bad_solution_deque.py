"""Solution timeouts due to O(N) rotation - finding the element in the middle"""

from collections import deque

N = int(input())
dlist = deque()

for _ in range(N):
    args = input().split()
    
    if args[0] == "add":
        x = int(args[1])
        dlist.append(x)
    
    elif args[0] == "gun":
        dlist.pop()
        
    elif args[0] == "milen":
        dlist.rotate(-(len(dlist)//2))
        
print(len(dlist))
print(*dlist)