class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            elif mid_val < target:
                left += 1
            else:
                right -= 1
        return -1