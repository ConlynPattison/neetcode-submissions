# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_seen = 0

        def dbt(node: Optional[TreeNode]) -> int:
            nonlocal max_seen

            if node is None: return -1

            left_dist = dbt(node.left) + 1
            right_dist = dbt(node.right) + 1

            diameter_at_node = left_dist + right_dist
            max_seen = max(max_seen, diameter_at_node)

            return max(left_dist, right_dist)

        dbt(root)
        return max_seen