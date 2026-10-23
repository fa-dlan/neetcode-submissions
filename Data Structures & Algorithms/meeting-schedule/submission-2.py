"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        n = len(intervals)
        intervals.sort(key = lambda inv: inv.start)
        end = intervals[0].end
        for i in range(1, n):
            cur = intervals[i]
            a = cur.start
            b = cur.end
            if end > a:
                return False
            end = b
        return True