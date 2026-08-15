class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[-1]
        def f(arr):
            cache = [-1] * n
            def dp(i):
                if i >= n-1:
                    return 0
                if cache[i] != -1:
                    return cache[i]
                take = arr[i] + dp(i+2)
                notTake = dp(i+1)
                cache[i] = max(take,notTake)
                return cache[i]
            return dp(0)
        return max(f(nums[:-1]),f(nums[1:]))