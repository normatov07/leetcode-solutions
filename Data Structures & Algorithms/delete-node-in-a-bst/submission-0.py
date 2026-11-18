# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findLeftNode(self, root):
        if root.right is None:
            return root

        return self.findLeftNode(root.right)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return root
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left
            
            leftNode = self.findLeftNode(root.left)
            root.val, leftNode.val = leftNode.val, root.val
            root.left = self.deleteNode(root.left, key)
       
        return root
