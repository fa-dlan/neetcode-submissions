"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        m = {}
        def dfs(node):
            if node.val in m:
                return m[node.val]
            m[node.val] = Node(node.val)
            for neighbor in node.neighbors:
                cloned_neighbor = dfs(neighbor)
                m[node.val].neighbors.append(cloned_neighbor)
            return m[node.val]

        return dfs(node)