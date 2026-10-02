class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        out = []

        m = len(heights)
        n = len(heights[0])

        # build water flow for one direction
        def build_flow(dy, dx):
            flow = [[False] * n for _ in range(m)]

            for y in range(m):
                for x in range(n):
                    ny = y + dy
                    nx = x + dx

                    if (
                        0 <= ny < m
                        and 0 <= nx < n
                        and heights[y][x] >= heights[ny][nx]
                    ):
                        flow[y][x] = True

            return flow

        # build all water flows
        left = build_flow(0, -1)
        up = build_flow(-1, 0)
        right = build_flow(0, 1)
        down = build_flow(1, 0)

        flows = [
            (left, 0, -1),
            (up, -1, 0),
            (right, 0, 1),
            (down, 1, 0)
        ]

        pac = [[False] * n for _ in range(m)]
        atl = [[False] * n for _ in range(m)]

        visited = set()

        # pacific boundary
        def pac_boundary(y, x):
            return y == 0 or x == 0

        # atlantic boundary
        def atl_boundary(y, x):
            return y == m - 1 or x == n - 1

        # dfs to ocean
        def dfs_flow(y, x, ocean, is_boundary):
            # memo
            if ocean[y][x]:
                return

            # visited
            if (y, x) in visited:
                return
            visited.add((y, x))

            # reached ocean
            if is_boundary(y, x):
                ocean[y][x] = True
                return

            # dfs all directions
            for flow, dy, dx in flows:
                ny = y + dy
                nx = x + dx

                # bounds
                if not (0 <= ny < m and 0 <= nx < n):
                    continue

                # water cannot flow
                if not flow[y][x]:
                    continue

                dfs_flow(ny, nx, ocean, is_boundary)

                # neighbor can reach ocean
                if ocean[ny][nx]:
                    ocean[y][x] = True
                    return

        # compute pac & atl
        for y in range(m):
            for x in range(n):
                visited.clear()
                dfs_flow(y, x, pac, pac_boundary)

                visited.clear()
                dfs_flow(y, x, atl, atl_boundary)

        # compute out
        for y in range(m):
            for x in range(n):
                if pac[y][x] and atl[y][x]:
                    out.append([y, x])

        return out