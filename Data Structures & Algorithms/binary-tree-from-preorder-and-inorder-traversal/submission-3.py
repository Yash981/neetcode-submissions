# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preOrder -> root, left, right
        #inorder - left , root, right
        #[1,2,3,4,5,6,7]
        #pre - 1,2,4,5,3,6,7
        #in - 4,2,5,1,6,3,7
        n = len(inorder)
        inorder_index = {
            value: i
            for i, value in enumerate(inorder)
        }
        index = 0
        def dfs(i,j):
            nonlocal index
            if i >= j:
                return None
            val = preorder[index]
            root = TreeNode(val)
            mid = inorder_index[val]
            index += 1
            root.left = dfs(i,mid)
            root.right = dfs(mid+1,j)
            return root
        return dfs(0,n)
            
