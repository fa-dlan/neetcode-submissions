class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # pattern: sliding window
        # cuz sliding window: shoul be O(n*2)

        n = len(nums)
        out = nums[0]

        def f():
            nonlocal out
            cur_pos = None
            cur_neg = None
            for x in nums:
                if x > 0:
                    if not cur_pos:
                        cur_pos = 1
                    if not cur_neg:
                        cur_neg = 1
                    cur_pos *= x
                    cur_neg *= x
                    out = max(out, cur_pos, cur_neg)
                elif x < 0:
                    if not cur_neg:
                        cur_neg = 1
                    cur_pos = None
                    cur_neg *= x
                    out = max(out, cur_neg)
                else:
                    cur_pos = None
                    cur_neg = None
                    out = max(out, 0)

        f()
        nums = nums[::-1]
        f()
        return out