class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            l = i+1
            r = n-1
            while l < r:
                if curr + nums[l] + nums[r] == 0:
                    ans.add((curr,nums[l],nums[r]))
                    l += 1
                    r -= 1
                elif curr + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1
        return [list(x) for x in ans]