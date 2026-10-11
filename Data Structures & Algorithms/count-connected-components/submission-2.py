class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        tree = {}
        for node in range(n):
            tree[node] = node

        def root(node):
            while tree[node] != node:
                node = tree[node]
            return node

        for a, b in edges:
            root_a = root(a)
            root_b = root(b)
            if root_a != root_b:
                tree[root_a] = root_b

        out = 0
        for node in range(n):
            if tree[node] == node:
                out += 1
        return out
