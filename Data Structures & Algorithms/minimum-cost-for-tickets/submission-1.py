from functools import lru_cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        # @lru_cache(None)
        # def dp(i):
        #     if i >= n:
        #         return 0
        #     #1-day
        #     res = costs[0] + dp(i+1)
        #     #2-day
        #     target = days[i] + 7
        #     index = i
        #     while index < n and days[index] < target:
        #         index += 1
        #     res = min(res,costs[1]+dp(index))

        #     #30-day
        #     target2 = days[i] + 30
        #     index2 = i
        #     while index2 < n and days[index2] < target2:
        #         index2 += 1
        #     res = min(res,costs[2]+dp(index2))
        #     return res
        # return dp(0)
        dp = [1e9] * (n+1)
        dp[n] = 0
        for i in range(n-1,-1,-1):
            for d,c in zip([1,7,30],costs):
                targetDay = days[i] + d
                new_i = i
                while new_i < n and days[new_i] < targetDay:
                    new_i += 1
                dp[i] = min(dp[i],c+dp[new_i])
        return dp[0]