class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        visited = set()

        def bfs(cord, i):
            y, x = cord
            if (
                cord in visited or
                y < 0 or y >= m or
                x < 0 or x >= n or
                board[y][x] != word[i]
            ):
                return False
            if i == len(word) - 1:
                return True
            print(cord, board[y][x])
            visited.add(cord)
            adjs = (
                (y, x - 1),
                (y - 1, x),
                (y, x + 1),
                (y + 1, x),
            )
            for adj in adjs:
                if bfs(adj, i + 1):
                    return True
            visited.discard(cord)
            return False
            
        for y in range(m):
            for x in range(n):
                if bfs((y, x), 0):
                    return True
        return False