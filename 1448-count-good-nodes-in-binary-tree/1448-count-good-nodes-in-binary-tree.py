# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def goodNodes(self, root: TreeNode, currMax=float('-inf')) -> int:
        #we need to check each root to leaf and keep track of the highest number
        if not root:
            return 0
        
        if root.val >= currMax:
            good = 1
        else:
            good = 0
        currMax = max(currMax, root.val)

        good += self.goodNodes(root.left, currMax)
        good += self.goodNodes(root.right, currMax)

        return good
        
    


        
