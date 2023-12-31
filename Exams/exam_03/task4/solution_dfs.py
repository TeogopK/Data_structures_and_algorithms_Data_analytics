class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.level = None

def insert(root, val):
    if not root:
        return Node(val)
    
    if root.val < val:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)
        
    return root

def dfs(root, depth, result):
    if not root:
        return
    
    dfs(root.left, depth + 1, result)
    dfs(root.right, depth + 1, result)
    
    result[depth] += 1

def count_nodes(root):
    result = [0] * 1_000_000
    dfs(root, depth = 0, result = result)

    result = [value for value in result if value]
    print(*result, sep=';')

arr = list(map(int, input().split()))[1:]

root = None
for value in arr:
    root = insert(root, value)

count_nodes(root)
