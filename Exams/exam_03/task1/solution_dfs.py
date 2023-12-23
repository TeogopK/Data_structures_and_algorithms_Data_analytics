class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return Node(val)
    
    if root.val < val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
        
    return root

def dfs(root, result):
    if not root:
        return
    
    dfs(root.right, result)
    dfs(root.left, result)
    result.append(root.val)

def print_nodes(root):
    result = []
    dfs(root, result)
    print(*result, sep=';')

N = int(input())

root = None
for _ in range(N):
    root = insert(root, int(input()))

print_nodes(root)