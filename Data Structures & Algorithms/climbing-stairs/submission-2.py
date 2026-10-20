class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def r(n):
            if n in memo:
                return memo[n]

            if n < 0:
                return 0
            elif n == 0:
                return 1
            step = r(n - 2) + r(n - 1)
            memo[n] = step
            return step
        
        return r(n)