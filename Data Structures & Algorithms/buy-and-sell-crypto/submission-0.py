class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        lowest = prices[0]
        for i in range(len(prices)):
            today = prices[i]
            if today < lowest:
                lowest = today
            else:
                out = max(out, today - lowest)
        return out