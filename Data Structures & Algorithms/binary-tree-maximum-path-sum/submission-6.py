# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -1e9
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(0,left)
            rightMax = max(0,right)
            ans = max(ans,root.val + leftMax + rightMax)
            return max(leftMax,rightMax) + root.val 
        dfs(root)
        return ans