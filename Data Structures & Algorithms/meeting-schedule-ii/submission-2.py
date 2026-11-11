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
        intervals.sort(key = lambda inv: inv.start)

        ends = [intervals[0].end]
        for inv in intervals[1:]:
            min_end = heapq.heappop(ends)
            if min_end > inv.start:
                heapq.heappush(ends, min_end)
            heapq.heappush(ends, inv.end)

        return len(ends)