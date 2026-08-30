class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 0:
            return 0
        i = 0
        j = 0
        currPro = 1
        ans = 0
        while j < n:
            currPro *= nums[j]
            while i <= j and currPro >= k:
                currPro //= nums[i]
                i += 1
            length = j - i + 1
            ans += length 
            j += 1
        return ans