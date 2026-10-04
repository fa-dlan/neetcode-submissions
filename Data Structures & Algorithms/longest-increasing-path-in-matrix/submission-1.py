class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        memo = {}
        highest_val = max(max(row) for row in matrix)

        def dfs(cords):
            # already computed
            if cords in memo:
                return

            y, x = cords
            val = matrix[y][x]

            # check left, up, right, down
            adjs = [
                (y, x - 1),
                (y - 1, x),
                (y, x + 1),
                (y + 1, x)
            ]

            higher_adjs = []

            for adj_y, adj_x in adjs:
                # make sure coordinate is valid
                if 0 <= adj_y < m and 0 <= adj_x < n:
                    # only move to strictly higher value
                    if matrix[adj_y][adj_x] > val:
                        higher_adjs.append((adj_y, adj_x))

            # base case: no higher adjacent cells
            if not higher_adjs:
                memo[cords] = 1
                return

            # dfs all higher adjacent cells
            for adj in higher_adjs:
                dfs(adj)

            # current cell + longest path from its higher neighbors
            memo[cords] = 1 + max(memo[adj] for adj in higher_adjs)

        # run dfs from every coordinate
        for y in range(m):
            for x in range(n):
                dfs((y, x))

        return max(memo.values())