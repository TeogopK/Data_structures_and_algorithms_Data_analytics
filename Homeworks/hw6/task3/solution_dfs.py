class Node:
    def __init__(self, val, left=-1, right=-1):
        self.val = val
        self.left = left
        self.right = right
         

def dfs(indx = 0, longest_so_far = -(10 ** 5)):
    if indx == -1:
        return 0, longest_so_far
    
    root = arr[indx]
    
    L, longestL = dfs(root.left, longest_so_far)
    R, longestR = dfs(root.right, longest_so_far)
    
    max_as_part = max(L + root.val, R + root.val, root.val)
    max_as_root = max(L + R + root.val, max_as_part)
    
    longest_so_far = max(longestL, longestR, max_as_root)
    
    return max_as_part, longest_so_far
       
        
N = int(input())
arr = [Node(*map(int, input().split())) for _ in range(N)]

_, longest = dfs()

print(longest)