# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        out = -float('inf')

        def r(node):
            nonlocal out

            if not node:
                return -float('inf')
            
            cur = node.val
            left = r(node.left)
            right = r(node.right)

            max_include_node = max(left + cur, right + cur, cur)
            out = max(out, max_include_node, left + cur + right)
            return max_include_node

        r(root)
        return out