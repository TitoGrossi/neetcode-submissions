# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal diameter

            if not node:
                return 0

            max_path_length_left = dfs(node.left)
            max_path_length_right = dfs(node.right)

            diameter = max(diameter, max_path_length_left + max_path_length_right)

            return max(max_path_length_left, max_path_length_right) + 1 

        dfs(root) 

        return diameter