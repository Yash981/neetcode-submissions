class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        ans = nums[0]
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                ans = min(ans,nums[mid])
                r = mid - 1
        # print(l,r)
        return ans
        
        

            
            
