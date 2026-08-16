from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            #1-day
            res = costs[0] + dp(i+1)
            #2-day
            target = days[i] + 7
            index = i
            while index < n and days[index] < target:
                index += 1
            res = min(res,costs[1]+dp(index))

            #30-day
            target2 = days[i] + 30
            index2 = i
            while index2 < n and days[index2] < target2:
                index2 += 1
            res = min(res,costs[2]+dp(index2))
            return res
        return dp(0)