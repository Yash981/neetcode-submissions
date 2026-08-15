class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        def backtrack(i,stack):
            ans.add(tuple(sorted(stack[:])))
            for x in range(i,n):
                stack.append(nums[x])
                backtrack(x+1,stack)
                stack.pop()
        backtrack(0,[])
        return [list(x) for x in ans]