class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        find = set()
        out = nums[0]
        for x in nums:
            if x in find:
                out = x
                break
            else:
                find.add(x)
        return out
        