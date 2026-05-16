# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hmap = {val:ind for ind,val in enumerate(inorder)}
        self.pre_ind = 0
        def dfs(left,right):
            if left > right:
                return None
            root = TreeNode(preorder[self.pre_ind])
            ind = hmap[preorder[self.pre_ind]]
            self.pre_ind+=1
            root.left = dfs(left,ind-1)
            root.right = dfs(ind+1,right)
            return root
        return dfs(0,len(inorder)-1)
