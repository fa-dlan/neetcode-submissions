class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        out = []

        m = len(heights)
        n = len(heights[0])

        left, up, right, down, pac, atl = [
            [[False] * n for _ in range(m)] for _ in range(6)
        ]

        # build left
        for y in range(m):
            for x in range(n):
                if x == 0 or heights[y][x] >= heights[y][x - 1]:
                    left[y][x] = True

        # build right
        for y in range(m):
            for x in range(n - 1, -1, -1):
                if x == n - 1 or heights[y][x] >= heights[y][x + 1]:
                    right[y][x] = True

        # build up
        for x in range(n):
            for y in range(m):
                if y == 0 or heights[y][x] >= heights[y - 1][x]:
                    up[y][x] = True

        # build down
        for x in range(n):
            for y in range(m - 1, -1, -1):
                if y == m - 1 or heights[y][x] >= heights[y + 1][x]:
                    down[y][x] = True

        visited = set()

        def dfs_pac(y, x):
            # memo
            if pac[y][x]:
                return

            # visited
            if (y, x) in visited:
                return
            visited.add((y, x))

            # pacific boundary
            if x == 0 or y == 0:
                pac[y][x] = True
                return

            # left dfs
            if x > 0 and left[y][x]:
                dfs_pac(y, x - 1)
                if pac[y][x - 1]:
                    pac[y][x] = True
                    return

            # up dfs
            if y > 0 and up[y][x]:
                dfs_pac(y - 1, x)
                if pac[y - 1][x]:
                    pac[y][x] = True
                    return

            # right dfs
            if x < n - 1 and right[y][x]:
                dfs_pac(y, x + 1)
                if pac[y][x + 1]:
                    pac[y][x] = True
                    return

            # down dfs
            if y < m - 1 and down[y][x]:
                dfs_pac(y + 1, x)
                if pac[y + 1][x]:
                    pac[y][x] = True
                    return

        def dfs_atl(y, x):
            # memo
            if atl[y][x]:
                return

            # visited
            if (y, x) in visited:
                return
            visited.add((y, x))

            # atlantic boundary
            if x == n - 1 or y == m - 1:
                atl[y][x] = True
                return

            # right dfs
            if x < n - 1 and right[y][x]:
                dfs_atl(y, x + 1)
                if atl[y][x + 1]:
                    atl[y][x] = True
                    return

            # down dfs
            if y < m - 1 and down[y][x]:
                dfs_atl(y + 1, x)
                if atl[y + 1][x]:
                    atl[y][x] = True
                    return

            # left dfs
            if x > 0 and left[y][x]:
                dfs_atl(y, x - 1)
                if atl[y][x - 1]:
                    atl[y][x] = True
                    return

            # up dfs
            if y > 0 and up[y][x]:
                dfs_atl(y - 1, x)
                if atl[y - 1][x]:
                    atl[y][x] = True
                    return

        # compute pac & atl
        for y in range(m):
            for x in range(n):
                visited.clear()
                dfs_pac(y, x)

                visited.clear()
                dfs_atl(y, x)

        # compute out
        for y in range(m):
            for x in range(n):
                if pac[y][x] and atl[y][x]:
                    out.append([y, x])

        return out