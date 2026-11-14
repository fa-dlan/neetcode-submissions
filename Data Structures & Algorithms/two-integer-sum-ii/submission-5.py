class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        # def search_index(val):
        #     left, right = 0, n - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if numbers[mid] == val:
        #             return mid
        #         elif numbers[mid] < val:
        #             left = mid + 1
        #         else:
        #             right = mid - 1
        #     return -1
        
        left = 0
        right = n - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1
        return []