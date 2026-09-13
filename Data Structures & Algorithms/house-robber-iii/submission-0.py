# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import lru_cache
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @lru_cache(None)
        def dp(root):
            if not root:
                return 0
            res = root.val
            if root.left:
                res += dp(root.left.left)
                res += dp(root.left.right)
            if root.right:
                res += dp(root.right.left)
                res += dp(root.right.right)
            res = max(res,dp(root.left)+dp(root.right))
            return res
        return dp(root)