# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Simple DFS algorithm for constructing the lexiographically smallest leaf-to-root string in a binary tree
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:

        def dfs(root, parentVal):
            if not root:
                return ''
            #left returns the lexiographically smallest string on the left side
            rootLetter = chr(97 + int(root.val))
            left = dfs(root.left, rootLetter + parentVal)
            right = dfs(root.right, rootLetter + parentVal)
            if not left:
                return right + rootLetter
            if not right:
                return left + rootLetter
            leftString = left + rootLetter + parentVal
            rightString = right + rootLetter + parentVal
            if leftString <= rightString:
                return left + rootLetter
            return right + rootLetter
        
        res = dfs(root, "")
        print(res)
        return res