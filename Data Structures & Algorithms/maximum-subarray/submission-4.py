class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        out =  nums[0]

        # expand right until its < 0
        left = 0
        while left < n:
            cur = 0
            for right in range(left, n):
                cur += nums[right]
                out = max(out, cur)
                if cur < 0:
                    left = right
                    break
            else:
                break
            left += 1
        return out