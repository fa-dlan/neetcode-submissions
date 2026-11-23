class Solution:
    def check_root(self, node, sub_node):
        if not node and not sub_node:
            return True
        if not node or not sub_node or node.val != sub_node.val:
            return False

        return (
            self.check_root(node.left, sub_node.left)
            and self.check_root(node.right, sub_node.right)
        )

    def check_same(self, node, subRoot):
        return self.check_root(node, subRoot)

    def traverse(self, node, subRoot):
        if not node:
            return False

        if self.check_same(node, subRoot):
            return True

        return (
            self.traverse(node.left, subRoot)
            or self.traverse(node.right, subRoot)
        )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.traverse(root, subRoot)