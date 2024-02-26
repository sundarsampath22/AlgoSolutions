# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
#
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def isSimilar(p, q):
            if (p and not q) or (not p and q):
                return False
            if (not p and not q):
                return True
            leftSideSame = isSimilar(p.left, q.left)
            rightSideSame = isSimilar(p.right, q.right)
            return leftSideSame and rightSideSame and (p.val == q.val)

        return isSimilar(p, q)