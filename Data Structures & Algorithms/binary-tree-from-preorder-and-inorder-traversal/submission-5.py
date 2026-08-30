# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        indexMapping = Counter()
        for i,x in enumerate(inorder):
            indexMapping[x] = i
        index = 0
        def dfs(i,j):
            nonlocal index
            if i >= j:
                return None
            val = preorder[index]
            idx = indexMapping[val]
            index += 1
            root = TreeNode(val) 
            root.left = dfs(i,idx)
            root.right = dfs(idx+1,j)
            return root
        return dfs(0,n)
