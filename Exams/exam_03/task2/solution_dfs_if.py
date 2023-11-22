class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def dfs(root, result):
    if not root:
        return
    
    if root.left:
        result[-1] += 1
        dfs(root.left, result)
        
    if root.right:
        result[1] += 1
        dfs(root.right, result)
        
def insert(root, val):
    if not root:
        return Node(val)
    
    if root.val < val:
        root.right = insert(root.right, val)
    else: 
        root.left = insert(root.left, val)
        
    return root
        
def get_input():
    """
    If the example test case was not on two lines input can be accessed as:
    arr = list(map(int, input().split()))[1:]
    """
    
    arr = list(map(int, input().split()))

    if len(arr) == 1:
        return list(map(int, input().split()))
    
    return arr[1:]

arr = get_input()

root = None
for x in arr:
    root = insert(root, x)
 
result = {-1: 0, 1: 0}
dfs(root, result)

left = result[-1]
right = result[1]

print(f'[{left},{right}]')