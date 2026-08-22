from typing import Deque, Tuple, Dict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(Deque, self, val=0, left=None, righ, Tuplet=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parents = self.__construct_parents(root)
        p_depth = self.__find_depth(root, p)
        q_depth = self.__find_depth(root, q)

        while p_depth > q_depth:
            p = parents[p.val]
            p_depth -= 1
        
        while q_depth > p_depth:
            q = parents[q.val]
            q_depth -= 1

        while p is not q:
            p = parents[p.val]
            q = parents[q.val]

        return p

    @staticmethod
    def __construct_parents(root: TreeNode) -> Dict[int, TreeNode]:
        parents: Dict[int, TreeNode] = {}
        def dfs(parent, node: Optional[TreeNode]):
            if not node:
                return

            parents[node.val] = parent
            dfs(node, node.left)
            dfs(node, node.right)

        dfs(root, root)
        return parents

    @staticmethod 
    def __find_depth(root: TreeNode, node: TreeNode) -> int:
        queue: Deque[Tuple[int, TreeNode]] = deque([(0, root)])
        while queue:
            depth, popped_node = queue.popleft()
            if popped_node is node:
                return depth
            if popped_node.left:
                queue.append((depth + 1, popped_node.left))
            if popped_node.right:
                queue.append((depth + 1, popped_node.right))

        return -1
