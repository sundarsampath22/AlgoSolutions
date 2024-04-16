# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        #bfs search to depth (depth - 1), for each node, rearrange its left and right subtrees
        if not root:
            return TreeNode(val)
        if depth == 1:
            return TreeNode(val, root)
        tempRoot = root
        curDepth = 1
        queue = deque()
        queue.append(root)
        while queue:
            for _ in range(len(queue)):
                curNode = queue.popleft()
                if curDepth == depth - 1:
                    tempLeft = curNode.left
                    tempRight = curNode.right
                    newNodeLeft = TreeNode(val)
                    newNodeRight = TreeNode(val)
                    curNode.left = newNodeLeft
                    curNode.right = newNodeRight
                    newNodeLeft.left = tempLeft
                    newNodeRight.right = tempRight
                else:
                    if curNode.left:
                        queue.append(curNode.left)
                    if curNode.right:
                        queue.append(curNode.right)
            curDepth += 1
        return tempRoot