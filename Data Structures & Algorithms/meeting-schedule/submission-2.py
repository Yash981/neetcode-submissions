"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i:i.start)
        n = len(intervals)
        if n==0: return True
        prevEnd = intervals[0].end
        for i in range(1,n):
            currStart = intervals[i].start
            currEnd = intervals[i].end
            if prevEnd > currStart:
                return False
            prevEnd = currEnd
        return True
