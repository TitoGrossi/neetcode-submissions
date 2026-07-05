"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events: List[Tuple[int, bool]] = [] # (time, is_end)
        for interval in intervals:
            events.append((interval.start, False))
            events.append((interval.end, True))
        events.sort()

        max_conflicting_meetings, meetings = 0, 0
        for idx, (event_time, is_end) in enumerate(events):
            if is_end:
                meetings -= 1
            else:
                meetings += 1

            if idx + 1 < len(events) and events[idx + 1][0] == event_time:
                continue
                
            max_conflicting_meetings = max(max_conflicting_meetings, meetings)

        return max_conflicting_meetings
