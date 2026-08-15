class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i,stack):
            if sum(stack) == target:
                ans.append(stack[:])
                return
            if i >= len(nums):
                return
            if sum(stack) > target:
                return;
            stack.append(nums[i])
            unlimited = backtrack(i,stack)
            stack.pop()
            notTake = backtrack(i+1,stack)
        backtrack(0,[])
        return ans