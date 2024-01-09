class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Sort o(nlogn)
        sorted_intervals = sorted(intervals, key = lambda x:x[0])

        # result
        result = []

        for interval in sorted_intervals:
            if len(result) == 0 or result[-1][1] <= interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        
        return True if len(result) == len(intervals) else False