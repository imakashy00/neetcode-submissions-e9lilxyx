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
        intervals.sort(key=lambda x: x.start)
        print(intervals)
        merged = [intervals[0]]
        for interval in intervals[1:]:
            prev_start, prev_end = merged[-1].start, merged[-1].end
            curr_start, curr_end = interval.start, interval.end

            if curr_start < prev_end:
                merged[-1].end = max(curr_end,prev_end)
            else:
                merged.append(interval)
        return len(merged) == len(intervals)