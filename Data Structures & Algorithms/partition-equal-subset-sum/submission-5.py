class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # obvious bruteforce: O(2^n)
        # possible acceptable: O(n^2)
        
        # obvious case: only even sum, always false on odd sum
        # obvious case: sum of 1 subset is half of total sum

        s = sum(nums)
        if s % 2 == 1:
            return False
        
        n = len(nums)
        target = s // 2

        dp = [[True] + [False] * target for _ in range(n + 1)]

        for i in range(1, n):
            for j in range(1, target + 1):
                print(i)
                if (dp[i - 1][j] or
                    j - nums[i] >= 0 and dp[i - 1][j - nums[i]]
                ):
                    dp[i][j] = True
            if dp[i][-1]:
                return True

        return False