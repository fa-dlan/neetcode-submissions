"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        n = len(intervals)
        intervals.sort(key = lambda inv: inv.start)

        l = [intervals[0].end]
        for i in range(1, n):
            cur = intervals[i]
            a = cur.start
            b = cur.end

            min_end = heapq.heappop(l)
            # need more room
            if min_end > a:
                heapq.heappush(l, min_end)
            heapq.heappush(l, b)

        return len(l)