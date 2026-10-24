class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort(reverse=True)
        cut_i = -1
        for i in range(len(nums)):
            if nums[i] <= target:
                cut_i = i
                break
        if cut_i != -1:
            nums = nums[cut_i:]
        n = len(nums)
        out = []

        def f(i: int, cur: List[int], total: int):
            if total >= target:
                if total == target:
                    out.append(cur)
                return
            
            for j in range(i, n):
                app = cur.copy()
                app.append(nums[j])
                f(j, app, total + nums[j])

        for i in range(n):
            f(i, [nums[i]], nums[i])

        return out