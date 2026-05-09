# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p,q):
            if p is None and q is None:
                return True
            if p is None and q is not None or q is None and p is not None or p.val != q.val:
                return False
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        if root is None:
            return False
        if root.val == subRoot.val:
            return isSameTree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            