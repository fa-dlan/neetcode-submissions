class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        n = len(cost)
        out = 0

        def f(first_i):
            memo = {}
            def r(i):
                if i >= n:
                    return 0
                if i in memo:
                    return memo[i]
                one = cost[i] + r(i + 1)
                two = cost[i] + r(i + 2)
                memo[i] = min(one, two)
                return memo[i]
            
            return r(first_i)

        first = f(0)
        second = f(1)
        print(first, second)
        out = min(first, second)
        return out