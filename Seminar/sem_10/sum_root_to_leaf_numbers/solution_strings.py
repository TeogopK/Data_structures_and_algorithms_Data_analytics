# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = 

def dfs(current, s):
    if current is None:
        return []

    new_s = s + str(current.val)

    if current.left is None and current.right is None:
        return [new_s]

    lst = []

    if current.left is not None:
        lst.extend(dfs(current.left, new_s))
    
    if current.right is not None:
        lst.extend(dfs(current.right, new_s))

    return lst

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return sum([int(x) for x in dfs(root, "")])