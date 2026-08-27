"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def dfs(root):
            if not root:
                return None
            if root == p:
                return p
            if root == q:
                return q
            l = dfs(root.left)
            r = dfs(root.right)
            if l == None:
                return r
            if r == None:
                return l
            return root
        return dfs(root)
