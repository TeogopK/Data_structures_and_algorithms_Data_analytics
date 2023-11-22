class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def dfs(root, result):
    if not root:
        return
    
    dfs(root.left, result)
    dfs(root.right, result)
    
    if not root.left and not root.right and root.val % 2 == 1:
        result.append(root.val)
        
def insert(root, val):
    if not root:
        return Node(val)
    
    if root.val < val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
        
    return root
        
N = int(input())

root = None
for _ in range(N):
    root = insert(root, int(input()))
 
result = []
dfs(root, result)
print(sum(result))