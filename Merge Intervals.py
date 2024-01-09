class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort o(nlogn)
        sorted_intervals = sorted(intervals, key = lambda x:x[0])

        # result
        result = []

        for interval in sorted_intervals:
            if len(result) == 0 or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result