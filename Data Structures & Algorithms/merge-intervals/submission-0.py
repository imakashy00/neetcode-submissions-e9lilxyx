class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        merged = [intervals[0]]

        for interval in intervals[1:]:
            prev_start, prev_end = merged[-1]
            curr_start, curr_end = interval[0], interval[1]
            if curr_start <= prev_end:
                merged[-1][1] = max(prev_end, curr_end)
            else:
                merged.append(interval)
        return merged