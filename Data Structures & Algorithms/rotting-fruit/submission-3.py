from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = set()
        out = 0
        q = deque()

        for y in range(m):
            for x in range(n):
                cur = grid[y][x]
                if cur == 1:
                    fresh.add((y, x))
                elif cur == 2:
                    q.append((y, x))

        def bfs():
            nonlocal out
            while q:
                for _ in range(len(q)):
                    y, x = q.popleft()
                    adjs = [
                        (y - 1, x),
                        (y, x + 1),
                        (y + 1, x),
                        (y, x - 1)
                    ]
                    for adj in adjs:
                        if adj in fresh:
                            fresh.remove(adj)
                            q.append(adj)
                if q:
                    out += 1
        bfs()               
        print(fresh)
        return -1 if fresh else out