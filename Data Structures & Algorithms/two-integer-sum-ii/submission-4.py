class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        
        def search_index(val):
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == val:
                    return mid
                elif numbers[mid] < val:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
        
        for i in range(n):
            remaining = target - numbers[i]
            second_idx = search_index(remaining)
            if second_idx != -1 and second_idx != i:
                return sorted([i + 1, second_idx + 1])

        return []