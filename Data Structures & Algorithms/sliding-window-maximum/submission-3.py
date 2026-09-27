from _heapq import heapreplace
import heapq
from os import remove

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        out = []
        pq = []
        # populate initial data
        window = {}
        for x in nums[:k]:
            heapq.heappush(pq, -x)
            if x not in window:
                window[x] = 1
            else:
                window[x] = window[x] + 1
        for i in range(n - k + 1):
            if i > 0:
                removed = nums[i - 1]
                added = nums[i + k - 1]

                if window[removed] == 1:
                    window.pop(removed)
                else:
                    window[removed] = window[removed] - 1
                
                if window.get(added):
                    window[added] = window[added] + 1
                else:
                    window[added] = 1

                heapq.heappush(pq, -nums[i + k - 1])
            while -pq[0] not in window:
                heapq.heappop(pq)
            out.append(-pq[0])
        return out