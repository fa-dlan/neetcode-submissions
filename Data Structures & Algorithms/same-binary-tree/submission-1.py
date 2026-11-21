# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        out = True
        def r(p, q):
            nonlocal out
            if (not out or
                not p and not q
            ):
                return
            if (p and not q or 
                not p and q or
                p and q and p.val != q.val
            ):
                out = False
                return
            r(p.left, q.left)
            r(p.right, q.right)
        
        r(p, q)
        return out