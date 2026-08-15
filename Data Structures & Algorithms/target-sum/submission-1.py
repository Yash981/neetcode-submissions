from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # cache = [[-1] * (target+1) for _ in range(n+1)]
        @lru_cache(None)
        def dp(i,currTarget):
            if i >= n:
                if currTarget == target:
                    return 1
                return 0
            # if cache[i][currTarget] != -1:
            #     return cache[i][currTarget]
            plus = dp(i+1,currTarget+nums[i])
            minus = dp(i+1,currTarget-nums[i])
            # cache[i][currTarget] = plus + minus
            return plus + minus
        return dp(0,0)