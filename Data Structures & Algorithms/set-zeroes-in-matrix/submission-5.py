class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])
        
        def set_none(i, j):
            # vertical
            if j < n:
                for row in range(m):
                    if matrix[row][j] != 0:
                        matrix[row][j] = None
            
            # horizontal
            if i < m:
                for col in range(n):
                    if matrix[i][col] != 0:
                        matrix[i][col] = None


        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    set_none(row, col)
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == None:
                    matrix[row][col] = 0