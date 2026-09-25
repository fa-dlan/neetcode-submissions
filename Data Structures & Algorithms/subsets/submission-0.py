class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out = []
        for sub in range(2 ** n):
            subset = []
            mask = format(sub, 'b')
            while len(mask) < n:
                mask = '0' + mask
            for i, on in enumerate(mask):
                if int(on):
                    subset.append(nums[i])
            out.append(subset)
        return out