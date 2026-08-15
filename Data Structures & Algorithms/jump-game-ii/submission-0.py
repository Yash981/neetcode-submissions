from functools import lru_cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        @lru_cache(maxsize=None)
        def dp(i):
            if i >= n-1:
                return 0
            res = 1e9
            for x in range(i+1,min(i+nums[i]+1,n)):
                res = min(res,1+dp(x))
            return res
        return dp(0)