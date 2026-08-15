class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        def backtrack(i,stack):
            ans.append(stack[:])
            for x in range(i,n):
                if x-1 >= i and nums[x] == nums[x-1]:continue
                stack.append(nums[x])
                backtrack(x+1,stack)
                stack.pop()
        backtrack(0,[])
        return ans