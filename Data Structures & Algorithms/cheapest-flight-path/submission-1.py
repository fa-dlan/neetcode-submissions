class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # brute force: do dfs at most k
        neighbors = {}
        for i, j, p in flights:
            if i not in neighbors:
                neighbors[i] = [(j, p)]
            else:
                neighbors[i].append((j, p))
        
        memo = {}
        def rec(node, k):
            out = 1_000_000
            if node == dst and k >= 0:
                return 0
            if not k:
                return out
            if (node, k) in memo:
                return memo[(node, k)]
            if node in neighbors:
                for neighbor, p in neighbors[node]:
                    out = min(out, p + rec(neighbor, k - 1))
            memo[(node, k)] = out
            return out
        
        minimum = rec(src, k + 1)
        if minimum == 1_000_000:
            return -1
        return minimum