class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                curr1 = nums[i]
                curr2 = nums[j]
                l = j+1
                r = n-1
                while l < r:
                    currsum = curr1 + curr2 + nums[l] + nums[r]
                    if currsum < target:
                        l  += 1
                    elif currsum > target:
                        r -= 1
                    else:
                        ans.append([curr1,curr2,nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l +=1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
        return ans



