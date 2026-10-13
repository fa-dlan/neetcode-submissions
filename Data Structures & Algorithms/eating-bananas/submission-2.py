import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        # found: k <= h, k - 1 > h
        # k > h: increase k
        # both k and k - 1 < h: decrease k
        if sum(piles) <= h:
            return 1

        def possible(k):
            t = 0
            for p in piles:
                t += math.ceil(p/k)
            return t <= h
        
        left = 1
        right = max(piles)
        k = 1
        while left <= right:
            k = (left + right) // 2
            if not possible(k):
                left = k + 1
            elif possible(k - 1):
                right = k - 1
            else:
                break
        return k