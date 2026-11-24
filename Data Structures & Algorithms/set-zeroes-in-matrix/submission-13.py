class Solution:
    def prn(self, matrix):
        for row in matrix:
            print(row)
        print()

    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])
       
        # self.prn(matrix)

        # firsts
        first_row_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_row_zero = True
                break
        first_col_zero = False
        for j in range(n):
            if matrix[0][j] == 0:
                first_col_zero = True
                break

        # rows
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    break
        # self.prn(matrix)
        
        # cols
        for j in range(1, n):
            for i in range(m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    break
        # self.prn(matrix)
        
        # set zero rows
        for i in range(1, m):
            if matrix[i][0] != 0:
                continue
            for j in range(n):
                matrix[i][j] = 0
        # self.prn(matrix)

        # set zero cols
        for j in range(1, n):
            if matrix[0][j] != 0:
                continue
            for i in range(m):
                matrix[i][j] = 0
        # self.prn(matrix)
        
        if first_row_zero:
            for i in range(m):
                matrix[i][0] = 0
        if first_col_zero:
            for j in range(n):
                matrix[0][j] = 0
