import bisect
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # nums=[14,4,6,6,20,8,5,6,8,12,6,10,14,9,17,16,9,7,14,11,14,15,13,11,10,18,13,17,17,14,17,7,9,5,10,13,8,5,18,20,7,5,5,15,19,14]
        # #exp : 272187084
        # target=22
        nums.sort()
        mod = 10**9+ 7
        ans = 0
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            if curr <= target:
                rem = target - curr
                index = bisect.bisect_right(nums,rem)
                vals = index - i -1
                if vals >= 0:
                    ans += pow(2,vals)
                    ans %= mod
        return ans % mod