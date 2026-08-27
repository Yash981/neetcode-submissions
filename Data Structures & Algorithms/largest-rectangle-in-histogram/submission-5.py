class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []
        left = [-1] * n
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                left[index] = i
            stack.append(i)
        stack2 = []
        right = [n] * n
        for i in range(n):
            while stack2 and heights[stack2[-1]] >= heights[i]:
                index = stack2.pop()
                right[index] = i
            stack2.append(i)
        # print(left)
        # print(right)
        ans = 0
        for i in range(n):
            ans = max(ans,heights[i] * (right[i]-left[i]-1))
        return ans
        