class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        q = len(queries)
        ans = []
        for i in range(q):
            res = 1e9
            for j in range(n):
                if intervals[j][0] <= queries[i] <= intervals[j][1]:
                    res = min(res,intervals[j][1]-intervals[j][0]+1)
            if res == 1e9:
                ans.append(-1)
            else:
                ans.append(res)
        return ans

