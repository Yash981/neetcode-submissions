class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cache = [[-1] * 2 for _ in range(n+1)]
        def dp(i,bought):
            if i >= n:
                return 0
            if cache[i][bought] != -1:
                return cache[i][bought]
            res = 0
            if bought:
                res = max(res,prices[i] + dp(i+1,False))
            else:
                res = max(res,dp(i+1,True)-prices[i])
            res = max(res,dp(i+1,bought))
            cache[i][bought] = res
            return res
        return dp(0,False)