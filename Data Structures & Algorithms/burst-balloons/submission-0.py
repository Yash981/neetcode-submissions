from functools import lru_cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        @lru_cache(None)
        def dp(i,j):
            if i >= j:
                return 0
            ans = 0
            for k in range(i+1,j):
                currPro = nums[i] * nums[k] * nums[j]
                ans = max(ans,currPro+dp(i,k)+dp(k,j))
            return ans
        return dp(0,n+1)


