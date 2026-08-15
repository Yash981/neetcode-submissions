class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        memo = {}
        def dp(i,prev):
            if i >= n:
                return 0
            if (i,prev) in memo:
                return memo[(i,prev)]
            res = 0
            if prev == None or prev == nums[i]:
                res = max(res,1 + dp(i+1,nums[i]+1))
            res=max(res,dp(i+1,prev))
            memo[(i,prev)] = res
            return res
        return dp(0,None)
