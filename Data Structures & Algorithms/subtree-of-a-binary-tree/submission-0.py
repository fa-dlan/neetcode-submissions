# Definition for a binary tree node.
from decimal import Subnormal
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_same(node):
            is_same = True
            def check_root(node, sub_node):
                nonlocal is_same
                if not is_same or not node and not sub_node:
                    return
                if bool(node) ^ bool(sub_node) or node.val != sub_node.val:
                    is_same = False
                    return
                check_root(node.left, sub_node.left)
                check_root(node.right, sub_node.right)
            check_root(node, subRoot)
            return is_same
            
        out = False
        def traverse(node):
            nonlocal out
            if out or not node:
                return
            if check_same(node):
                out = True
                return
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return out
