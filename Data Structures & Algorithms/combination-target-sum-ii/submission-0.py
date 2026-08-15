class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        ans = []
        def backtrack(i,stack):
            if sum(stack) == target:
                ans.append(stack[:])
                return
            if sum(stack) > target:
                return
            for x in range(i,n):
                if x-1 >= i and candidates[x] == candidates[x-1]:continue
                stack.append(candidates[x])
                backtrack(x+1,stack)
                stack.pop()
        backtrack(0,[])
        return ans
