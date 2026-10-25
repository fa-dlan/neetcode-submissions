class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = set(nums)
        out = 0

        while s:
            lowest = min(s)
            s.remove(lowest)

            temp = 1
            while lowest + 1 in s:
                lowest = lowest + 1
                s.remove(lowest)

                temp += 1
            out = max(out, temp)
        
        return out