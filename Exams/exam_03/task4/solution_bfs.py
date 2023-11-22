from collections import deque

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

def bfs(root):
    if not root:
        return [0]
    
    counts = []
    q = deque([root])
    
    while q:
        count = len(q)
        counts.append(count)  
        
        for _ in range(count):
            current = q.popleft()

            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)

    return counts

def count_nodes(root):
    counts = bfs(root)
    print(*counts, sep=';')

arr = list(map(int, input().split()))[1:]

root = None
for value in arr:
    root = insert(root, value)

count_nodes(root)
