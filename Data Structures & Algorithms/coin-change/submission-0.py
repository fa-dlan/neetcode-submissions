class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return 0
        n = len(coins)
        dp = [0] +[float('inf')] * (amount)

        for i in range(n):
            coin = coins[i]
            for j in range(1, amount + 1):
                if j - coin >= 0:
                    dp[j] = min(dp[j], 1 + dp[j - coin])
        
        out = dp[amount]
        if out == float('inf'):
            return -1
        else:
            return int(out)