class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        zero_rows = set()
        zero_cols = set()

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for rows in zero_rows:
            for cols in range(n):
                matrix[rows][cols] = 0
        
        for cols in zero_cols:
            for rows in range(m):
                matrix[rows][cols] = 0
        