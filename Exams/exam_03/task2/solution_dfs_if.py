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
    
    if root.left:
        result[-1] += 1
        dfs(root.left, result)
        
    if root.right:
        result[1] += 1
        dfs(root.right, result)

def left_right(root):
    result = {-1: 0, 1: 0}
    dfs(root, result)

    print(f'[{result[-1]},{result[1]}]')

arr = list(map(int, input().split()))[1:]

root = None
for value in arr:
    root = insert(root, value)

left_right(root)