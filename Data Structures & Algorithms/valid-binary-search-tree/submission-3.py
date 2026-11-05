# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def r(node):

            node_val = node.val

            left_valid, smallest_left_val, biggest_left_val = True, node_val, -float('inf')
            if node.left:
                left_valid, smallest_left_val, biggest_left_val = r(node.left)

            right_valid, smallest_right_val, biggest_right_val = True, float('inf'), node_val
            if node.right:
                right_valid, smallest_right_val, biggest_right_val = r(node.right)
            
            is_valid = (
                    left_valid and
                    right_valid and
                    biggest_left_val < node_val < smallest_right_val
                )

            return (
                    is_valid,
                    smallest_left_val,
                    biggest_right_val,
                )
        
        return r(root)[0]