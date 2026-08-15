class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda i:i[0])
        print(intervals)
        stack = [intervals[0]]
        for i in range(1,n):
            currStart = intervals[i][0]
            currEnd = intervals[i][1]
            if stack and stack[-1][1] >= currStart:
                s,e = stack.pop()
                stack.append([min(s,currStart),max(e,currEnd)])
                continue
            stack.append([currStart,currEnd])

        return stack