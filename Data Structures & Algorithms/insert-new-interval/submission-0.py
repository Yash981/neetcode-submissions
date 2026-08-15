class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        # print(intervals)
        intervals.sort()
        n = len(intervals)
        stack = [intervals[0]]
        for i in range(1,n):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            if stack and stack[-1][1] >= currStart:
                s,e = stack.pop()
                stack.append([min(s,currStart),max(currEnd,e)])
            else:
                stack.append([currStart,currEnd])
        return stack
