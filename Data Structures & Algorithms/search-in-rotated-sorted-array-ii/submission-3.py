class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        r = n-1
        # while r-1 >= 0 and nums[r] == nums[r-1]:
        #     r -= 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                return True
            if nums[l] < nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
        return False
