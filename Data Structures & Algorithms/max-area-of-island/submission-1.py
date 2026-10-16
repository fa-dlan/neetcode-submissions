class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        out = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(cord):
            y, x = cord
            if (x < 0
                or y < 0
                or y >= m
                or x >= n
                or grid[y][x] == 0
            ):
                return 0
            
            grid[y][x] = 0
            
            adjs = [
                (y, x - 1),
                (y - 1, x),
                (y, x + 1),
                (y + 1, x)
            ]

            temp = 0
            for adj in adjs:
                temp += dfs(adj)
            
            return 1 + temp

        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    out = max(out, dfs((y, x)))
        return out