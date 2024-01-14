class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        resultIntervals = []
        for interval in intervals:
            if newInterval[0] > interval[1]:
                resultIntervals.append(interval)
            elif newInterval[1] < interval[0]:
                resultIntervals.append(newInterval)
                newInterval = interval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        resultIntervals.append(newInterval)
        return resultIntervals
