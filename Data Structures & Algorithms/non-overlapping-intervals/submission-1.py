class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        rem = 0
        last = intervals[0]
        for interval in intervals[1:]:
            last_start, last_end = last
            curr_start, curr_end = interval
            if curr_start < last_end:
                rem+= 1
            else:
                last = interval
        return rem