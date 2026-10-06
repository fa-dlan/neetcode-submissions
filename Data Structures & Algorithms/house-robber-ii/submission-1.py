class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        memo = [None] * len(nums)

        def rec(i):
            if i >= len(nums):
                return 0
            
            if memo[i]:
                return memo[i]

            take = nums[i] + rec(i + 2)
            skip = rec(i + 1)
            max_i = max(take, skip)
            memo[i] = max_i
            return max_i
        
        without_first = rec(1)
        nums = nums[:-1]
        memo = [None] * len(nums)
        without_last = rec(0)
        return max(without_first, without_last)
