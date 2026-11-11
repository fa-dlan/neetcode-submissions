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
        for start, end in map(lambda inv: (inv.start, inv.end), intervals[1:]):
            min_end = heapq.heappop(ends)
            if min_end > start:
                heapq.heappush(ends, min_end)
            heapq.heappush(ends, end)

        return len(ends)