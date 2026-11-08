class Solution:
    def trap(self, height: List[int]) -> int:
        # on every x, f(x) = max(0, min(max(left), max(right)) - y(x))
        # O(n*2)
        if not height:
            return 0
        n = len(height)
        out = 0

        left_highest = [0] * n
        right_highest = [0] * n
        
        # left to right pass
        highest = 0
        for i in range(n):
            highest = max(highest, height[i])
            left_highest[i] = highest

        # right to left pass
        highest = 0
        for i in range(n - 1, -1, -1):
            highest = max(highest, height[i])
            right_highest[i] = highest

        for i in range(n):
            out += max(0, min(left_highest[i], right_highest[i]) - height[i])

        return out