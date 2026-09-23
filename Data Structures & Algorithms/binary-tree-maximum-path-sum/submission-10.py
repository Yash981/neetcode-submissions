# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = root.val
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(0,left)
            rightMax = max(0,right)
            ans = max(ans,leftMax+rightMax+root.val)
            return max(rightMax,leftMax) + root.val
        dfs(root)
        return ans

