class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1] * n
        def dp(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]
            take = cost[i] + dp(i+1)
            take2 = cost[i] + dp(i+2)
            cache[i] = min(take,take2)
            return min(take,take2)
        return min(dp(0),dp(1))