class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = [-1] * n
        def dp(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]
            take = nums[i] + dp(i+2)
            notTake = dp(i+1)
            cache[i] = max(take,notTake)
            return max(take,notTake)
        return dp(0)