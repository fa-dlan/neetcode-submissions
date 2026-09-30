class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for _ in range(m)]
        memo[m - 1][n - 1] = 1

        def build(y, x):
            # already calculated
            if memo[y][x] != 0:
                return

            right, down = 0, 0

            if x < n - 1:
                build(y, x + 1)
                right = memo[y][x + 1]

            if y < m - 1:
                build(y + 1, x)
                down = memo[y + 1][x]

            memo[y][x] = right + down

        build(0, 0)
        return memo[0][0]