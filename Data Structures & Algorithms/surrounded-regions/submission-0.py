from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        pseudo:
        find O on perimeter, 
        each of those O, do bfs
        all other O change to X
        """
        not_surrounded = set()
        m = len(board)
        n = len(board[0])

        # find O in perimeter:
        for y in range(m):
            for x in range(n):
                if (board[y][x] == 'O' and (
                        y in (0, m - 1) or
                        x in (0, n - 1)
                    )
                ):
                    not_surrounded.add((y, x))
        
        # bfs from intial O in perimeter
        q = deque(not_surrounded.copy())
        while q:
            y, x = q.popleft()
            left, right, down, up = [None] * 4
            left_cor, right_cor, down_cor, up_cor = [None] * 4
            if x > 0:
                left = board[y][x - 1]
                left_cor = (y, x - 1)
            if x < n - 1:
                right = board[y][x + 1]
                right_cor = (y, x + 1)
            if y < m - 1:
                down = board[y + 1][x]
                down_cor = (y + 1, x)
            if y > 0:
                up = board[y - 1][x]
                up_cor = (y - 1, x)
            for neighbor, neighbor_cor in zip(
                (left, right, down, up), 
                (left_cor, right_cor, down_cor, up_cor)
            ):
                if neighbor == 'O' and neighbor_cor not in not_surrounded:
                    q.append(neighbor_cor)
                    not_surrounded.add(neighbor_cor)
        
        # override surrounded with X
        for y in range(m):
            for x in range(n):
                if board[y][x] == 'O' and (y, x) not in not_surrounded:
                    board[y][x] = 'X'