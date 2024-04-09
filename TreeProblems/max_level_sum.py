# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS traversal of Tree
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curLevel = 1
        maxSum = float('-inf')
        resLevel = 1
        queue = [root]
        while queue:
            temp = []
            curSum = 0
            for _ in range(len(queue)):
                node = queue.pop()
                curSum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            if curSum > maxSum:
                maxSum = curSum
                resLevel = curLevel
            queue = temp
            curLevel += 1
        return resLevel