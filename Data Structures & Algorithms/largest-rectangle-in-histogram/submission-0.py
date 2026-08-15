class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = []
        res = [-1] * n
        for i in range(n-1,-1,-1):
            while left and heights[left[-1]] > heights[i]:
                res[left.pop()] = i
            left.append(i)
        right = []
        res2 = [n] * n
        for i in range(n):
            while right and heights[right[-1]] > heights[i]:
                res2[right.pop()] = i
            right.append(i)
        ans = 0
        for i in range(n):
            l = i-res[i]
            r = res2[i] - i - 1
            ans = max(ans,(l+r)*heights[i])
        # print(res)
        # print(res2)
        return ans