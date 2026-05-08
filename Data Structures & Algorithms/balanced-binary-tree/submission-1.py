# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node: return 0
            le = height(node.left)
            ri = height(node.right)
            if le == -1 or ri == -1 or abs(le - ri) > 1:
                return -1
            return 1 + max(le,ri)
        return height(root) != -1


