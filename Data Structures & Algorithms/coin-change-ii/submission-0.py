class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        cache = [[-1] * (amount+1) for _ in range(n+1)]
        def dp(i,target):
            if i >= n:
                return 0
            if target == amount:
                return 1
            if cache[i][target] != -1:
                return cache[i][target]
            ans = 0
            for x in range(i,len(coins)):
                if target+coins[x] <= amount:
                    ans += dp(x,target+coins[x])
            cache[i][target] = ans
            return ans
        return dp(0,0)