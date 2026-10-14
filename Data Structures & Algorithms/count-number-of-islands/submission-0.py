class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # pseudo:
        # bfs: when 1: go all direction
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        
        visited = set()

        def bfs(cord):
            y, x = cord
            if (
                cord in visited or 
                x < 0 or
                y < 0 or
                x >= n or
                y >= m or
                grid[y][x] == '0'
            ):
                return
            
            visited.add(cord)
            
            adjs = [
                (y, x - 1),
                (y - 1, x),
                (y, x + 1),
                (y + 1, x)
            ]
            for adj in adjs:
                bfs(adj)

        out = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    if (y, x) not in visited:
                        out += 1
                    bfs((y, x))
        
        return out