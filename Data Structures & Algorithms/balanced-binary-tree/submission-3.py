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

        valid = True
        def validate(node):
            nonlocal valid
            if not valid:
                return
            if not node:
                return 0

            left_max_height = validate(node.left)
            if left_max_height == None:
                return
            right_max_height = validate(node.right)
            if right_max_height == None:
                return

            if abs(left_max_height - right_max_height) > 1:
                valid = False
                return
            
            return 1 + max(left_max_height, right_max_height)

        validate(root)
        return valid