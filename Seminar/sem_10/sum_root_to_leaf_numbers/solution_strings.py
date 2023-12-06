def dfs(current):
    if current is None:
        return []
 
    if current.left is None and current.right is None:
        return [str(current.val)]
 
    lst = []
 
    if current.left is not None:
        lst.extend([f"{str(current.val)}{num}" for num in dfs(current.left)])
 
    if current.right is not None:
        lst.extend([f"{str(current.val)}{num}" for num in dfs(current.right)])
 
    return lst
    
 
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return sum([int(num) for num in dfs(root)])