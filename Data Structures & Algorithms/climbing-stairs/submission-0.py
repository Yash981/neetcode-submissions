class Solution:
    def climbStairs(self, n: int) -> int:
        memo = Counter()
        def dp(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            take = dp(i+1)
            take2 = dp(i+2)
            memo[i] = take + take2
            return take + take2
        return dp(0)