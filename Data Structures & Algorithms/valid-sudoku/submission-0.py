class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = set([str(i) for i in range(1, 10)])

        def check_area(corners):
            low_y, high_y, low_x, high_x = corners
            visited = set()
            for y in range(low_y, high_y):
                for x in range(low_x, high_x):
                    cur = board[y][x]
                    if cur == '.':
                        continue
                    if (cur not in valid
                        or cur in visited
                    ):
                        return False
                    visited.add(cur)
            return True

        areas = []

        # make rows and cols:
        for i in range(9):
            areas.append((i, i + 1, 0, 9))
            areas.append((0, 9, i, i + 1))
        
        # make boxes:
        corners = [(0, 3), (3, 6), (6, 9)]
        for a, b in corners:
            for c, d in corners:
                areas.append((a, b, c, d))
        
        for area in areas:
            if not check_area(area):
                return False

        return True
                 