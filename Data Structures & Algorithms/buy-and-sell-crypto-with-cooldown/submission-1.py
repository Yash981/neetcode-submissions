class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = [[-1] * 2 for _ in range(n+1)]
        def dp(i,Bought):
            if i >= n:
                return 0
            if cache[i][Bought] != -1:
                return cache[i][Bought]
            ans = 0
            if Bought:
                ans = max(ans,prices[i] + dp(i+2,False))
            else:
                ans = max(ans,-prices[i] + dp(i+1,True))
            ans = max(ans,dp(i+1,Bought))
            cache[i][Bought] = ans
            return ans
        return dp(0,False)