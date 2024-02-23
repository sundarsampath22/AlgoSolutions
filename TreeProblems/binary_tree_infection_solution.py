# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        
        #returns two integers
        #1. The number of minutes it would take to to infect the entire tree once the infected node is the adjacent to the root
        #2. The number of minutes it takes to infect the parent of our root (-1 if unknown)
        def traverse(root, start):
            if not root:
                return 0, -1
            costToInfectLeftSubtree, costToInfectLeftNode = traverse(root.left, start)
            costToInfectRightSubtree, costToInfectRightNode = traverse(root.right, start)
            isInfectedNode = root.val == start
            if isInfectedNode:
                return max(costToInfectLeftSubtree, costToInfectRightSubtree), 0
            else:
                if costToInfectRightNode == -1 and costToInfectLeftNode == -1:
                    return max(costToInfectLeftSubtree, costToInfectRightSubtree) + 1, -1
                elif costToInfectRightNode == -1:
                    startupCost = costToInfectLeftNode + 1
                    infectionTime = max(costToInfectRightSubtree + startupCost, max(1,costToInfectLeftSubtree))
                    return infectionTime, costToInfectLeftNode + 1
                elif costToInfectLeftNode == -1:
                    startupCost = costToInfectRightNode + 1
                    infectionTime = max(costToInfectLeftSubtree + startupCost, max(1,costToInfectRightSubtree))
                    return infectionTime, costToInfectRightNode + 1


        cost, costToInfectRoot = traverse(root,start)
        return cost