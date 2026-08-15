class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        used = [False] * n
        def backtrack(stack):
            if len(stack) == n:
                ans.append(stack[:])
                return;
            for x in range(n):
                if not used[x]:
                    used[x] = True
                    stack.append(nums[x])
                    backtrack(stack)
                    stack.pop()
                    used[x] = False
        backtrack([])
        return ans

