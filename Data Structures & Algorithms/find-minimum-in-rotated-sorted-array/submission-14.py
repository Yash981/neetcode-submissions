class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        ans = nums[0]
        while l <= r:
            mid = l + (r-l)//2
            ans = min(ans,nums[mid])
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return ans