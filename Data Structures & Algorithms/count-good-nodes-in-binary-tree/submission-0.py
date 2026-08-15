# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root,mx):
            nonlocal ans
            if root is None:
                return
            if root.val >= mx:
                ans += 1
            mx = max(mx,root.val)
            dfs(root.left,mx)
            dfs(root.right,mx)
        dfs(root,root.val)
        return ans