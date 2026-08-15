class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[1])
        print(intervals)
        n = len(intervals)
        prevEnd = intervals[0][1]
        removed = 0
        for i in range(1,n):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            if prevEnd > currStart:
                removed += 1
                # prevEnd = min(prevEnd,currEnd)
                continue
            prevEnd = currEnd
        return removed