# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: TreeNode | None) -> bool:
        
        isBalanced, _ =  self.helper(root)

        return isBalanced

    def helper(self, root: TreeNode | None):
        if root is None:
            return True, 0
        
        leftBalance, leftCount = self.helper(root.left)
        
        if not leftBalance:
            return False, 0

        rightBalance, rightCount = self.helper(root.right)

        if not rightBalance:
            return False, 0
        
        if abs(rightCount - leftCount) > 1:
            return False, 0

        return True, 1+max(leftCount, rightCount)


       

        
        