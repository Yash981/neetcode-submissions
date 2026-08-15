from functools import lru_cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            oneStep = dp(i+1)
            twoStep = dp(i+2)
            return cost[i] + min(oneStep,twoStep)
        return min(dp(0),dp(1))