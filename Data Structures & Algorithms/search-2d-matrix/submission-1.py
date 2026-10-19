class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not target:
            return False

        m = len(matrix)
        n = len(matrix[0])

        # 0 index
        def cord_to_idx(cord):
            y, x = cord
            return y * n + x            
        
        def idx_to_cord(idx):
            y = idx // n
            x = idx % n
            return (y, x)
        
        def shift_right(cord, k):
            return idx_to_cord(cord_to_idx(cord) + k)

        left_cord = (0, 0)
        right_cord = (m - 1, n - 1)
        while cord_to_idx(left_cord) <= cord_to_idx(right_cord):
            left_idx = cord_to_idx(left_cord)
            right_idx = cord_to_idx(right_cord)

            mid_idx = (left_idx + right_idx) // 2
            mid_cord = idx_to_cord(mid_idx)
            mid_val = matrix[mid_cord[0]][mid_cord[1]]

            if mid_val == target:
                return True
            elif mid_val < target:
                left_cord = shift_right(mid_cord, 1)
            else:
                right_cord = shift_right(mid_cord, -1)
        
        return False