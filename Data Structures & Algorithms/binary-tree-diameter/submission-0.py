# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        out = 0

        def rec(node):
            nonlocal out

            if not node:
                return 0
            left, right = 0, 0
            if node.left:
                left = 1 + rec(node.left)
            if node.right:
                right = 1 + rec(node.right)
            out = max(out, left + right)
            return max(left, right)

        rec(root)
        return out