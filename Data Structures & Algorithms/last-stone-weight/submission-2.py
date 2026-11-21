import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
            
        heapq.heapify_max(stones)
        while stones:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            smashed = y - x
            if smashed:
                heapq.heappush_max(stones, smashed)
            if len(stones) == 1:
                return stones[0]
        return 0