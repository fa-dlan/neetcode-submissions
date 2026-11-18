class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # 3 scenarios: 1 zero, 2 zero, no zero
        n = len(nums)
        zero_index = -1
        product_exclude_zero = 1
        out = [0] * n

        for i in range(n):
            if nums[i] == 0:
                if zero_index != -1:
                    return out
                zero_index = i
            else:
                product_exclude_zero *= nums[i]
        
        if zero_index != -1:
            out[zero_index] = product_exclude_zero
            return out

        for i in range(n):
            out[i] = product_exclude_zero // nums[i]
            
        return out