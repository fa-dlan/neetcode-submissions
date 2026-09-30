class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]
        memo[m - 1][n - 1] = 1

        for y in range(m - 1, -1, -1):
            for x in range(n - 1, -1, -1):
                # not right edge: append right
                if x < n - 1:
                    memo[y][x] += memo[y][x + 1]
                # not down ege: append down
                if y < m - 1:
                    memo[y][x] += memo[y + 1][x]

        return memo[0][0]