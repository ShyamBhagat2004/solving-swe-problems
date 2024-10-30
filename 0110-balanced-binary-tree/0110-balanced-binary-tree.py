# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:


        def height(root):#will return a list

            if not root:
                return [True, 0]
            
            a = height(root.left)
            b = height(root.right)
            
            #need to return two things
            balanced = a[0] and b[0] and abs(a[1]-b[1]) <= 1
            return balanced, max(a[1], b[1])+1
            
            

        return height(root)[0]
            
        




       