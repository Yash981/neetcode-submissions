class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        def isPossible(D):
            i = 0
            count = 0
            while i < n-1:
                if nums[i+1] - nums[i] <= D:
                    count += 1
                    i += 2
                else:
                    i += 1
            return count >= p
        l = 0
        r = max(nums)
        ans = -1
        while l <= r:
            mid = l + (r-l)//2
            if isPossible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans