class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        unique = set()

        def make_mask(b):
            bin_string = format(b, 'b')
            filled_bin_string = ['0'] * (n - len(bin_string)) + list(bin_string)
            return list(map(int, filled_bin_string))

        for b in range(2 ** n):
            subset = []
            for i, on in enumerate(make_mask(b)):
                if on:
                    subset.append(nums[i])
            unique.add(tuple(subset))

        out = []
        for tup in unique:
            out.append(list(tup))
        return out