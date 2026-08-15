class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        if n==1:
            return nums[0]
        ans = 1e9
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                ans = min(ans,nums[mid])
                r = mid
        print(l,r)
        return nums[l]
        
        

            
            
