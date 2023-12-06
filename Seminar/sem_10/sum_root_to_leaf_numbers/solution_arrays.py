# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, path, all_paths):
        if not root.left and not root.right:
            all_paths.append(path)

        if root.left:
            self.dfs(root.left, path + [root.left.val], all_paths)

        if root.right:
            self.dfs(root.right, path + [root.right.val], all_paths)

    def get_list_as_number(self, arr):
        return int("".join(map(str, arr)))

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        all_paths = []
        self.dfs(root, [root.val], all_paths)

        return sum(self.get_list_as_number(path) for path in all_paths)