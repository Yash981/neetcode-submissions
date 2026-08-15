# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        globalMax = -1e9
        def dfs(root):
            nonlocal globalMax
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = root.val + max(left,right)
            globalMax = max(globalMax,res,root.val,left+right+root.val)
            return max(0,res)
        dfs(root)
        return globalMax