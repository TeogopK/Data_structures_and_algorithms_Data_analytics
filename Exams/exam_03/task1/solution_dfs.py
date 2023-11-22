"""
Solution ignoring the wrong template.
The main issue with the template is that it ignores duplicates,
while there are test cases with duplicates. 
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def dfs(root, result):
    if not root:
        return
    
    dfs(root.right, result)
    dfs(root.left, result)
    result.append(root.val)
        
def insert(root, val):
    if not root:
        return Node(val)
    
    if root.val < val:
        root.right = insert(root.right, val)
    else: # includes = 
        root.left = insert(root.left, val)
        
    return root
        
N = int(input())

root = None
for _ in range(N):
    root = insert(root, int(input()))
 
result = []
dfs(root, result)
print(*result, sep=';')