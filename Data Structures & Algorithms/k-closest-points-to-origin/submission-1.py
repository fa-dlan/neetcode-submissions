import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for point in points:
            distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
            heapq.heappush_max(pq, (distance, point))
            if len(pq) > k:
                heapq.heappop_max(pq)
        return list(map(lambda point: point[1], pq))