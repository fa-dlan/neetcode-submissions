class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        out = nums[0]

        # expand right until its < 0
        cur = 0
        for x in nums:
            cur += x
            out = max(cur, out)
            if cur < 0:
                cur = 0
        return out