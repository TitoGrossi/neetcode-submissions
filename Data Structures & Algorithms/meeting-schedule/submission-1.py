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
            
        intervals.sort(key = lambda x: (x.start, x.end))
        last_interval_end_time = intervals[0].start - 1
        for interval in intervals:
            if last_interval_end_time > interval.start:
                return False
            last_interval_end_time = interval.end

        return True
