from _heapq import heapify
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        max_heights = {None: 0}
        def populate_max_heights(node):
            if not node:
                return
            populate_max_heights(node.left)
            populate_max_heights(node.right)
            max_heights[node] = 1 + max(
                max_heights[node.left],
                max_heights[node.right]
            )

        populate_max_heights(root)

        valid = True
        def validate(node):
            nonlocal valid
            if not valid or not node:
                return
            if abs(max_heights[node.left] - max_heights[node.right]) > 1:
                valid = False
                return
            validate(node.left)
            validate(node.right)

        validate(root)
        return valid