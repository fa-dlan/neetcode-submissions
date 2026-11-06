class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        out = 0
        freq = {}
        if not nums:
            return 0
        n = len(nums)

        for x in nums:
            if x not in freq:
                freq[x] = 0
            else:
                freq[x] += 1
                out += freq[x]
        
        return out
        
