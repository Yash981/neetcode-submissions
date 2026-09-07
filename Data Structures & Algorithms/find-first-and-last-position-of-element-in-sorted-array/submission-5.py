import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # nums=[1,2,4,4,5,6]
        # target=3
        n = len(nums)
        if not nums:
            return [-1,-1]
        left = bisect.bisect_left(nums,target)
        if left >= n or nums[left] != target:
            return [-1,-1]
        right = bisect.bisect_right(nums,target) - 1
        
        if left != -1 and right != -1 and left < n and right < n:
            return [left,right]
        else:
            return [-1,-1]