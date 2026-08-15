class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def backtrack(i,stack):
            res.append(stack[:])
            for x in range(i,n):
                stack.append(nums[x])
                backtrack(x+1,stack)
                stack.pop()
        backtrack(0,[])
        return res