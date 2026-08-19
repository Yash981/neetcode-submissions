from functools import lru_cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        @lru_cache(None)
        def dp(i,bought):
            if i >= n:
                return 0
            ans = 0
            if bought:
                ans = max(ans,prices[i] + dp(i+1,not bought))
            else:
                ans = max(ans,dp(i+1,not bought)-prices[i])
            return max(ans,dp(i+1,bought))
        return dp(0,False)
            
