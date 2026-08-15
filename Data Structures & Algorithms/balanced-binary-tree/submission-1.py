# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if node is None:
                return True,0
            leftB,left = dfs(node.left)
            rightB,right = dfs(node.right)
            currentBalanced =  leftB and rightB and abs(left-right) <= 1
                
            return currentBalanced,max(left, right) + 1
        currentBalanced,_= dfs(root)
        return currentBalanced

            