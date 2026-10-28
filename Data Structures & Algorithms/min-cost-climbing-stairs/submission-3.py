class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        n = len(cost)

        def f(first_i):
            memo = {}
            def r(i):
                if i in memo:
                    return memo[i]
                if i >= n:
                    return 0
                memo[i] = cost[i] + min(r(i + 1), r(i + 2))
                return memo[i]
            return r(first_i)

        return min(f(0), f(1))