# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        preorderIndex = 0
        inorder_map = {value: key for key, value in enumerate(inorder)}
        
        def build(left, right):
            nonlocal preorderIndex
            
            if left > right:
                return None
            
            root_val = preorder[preorderIndex]
            root = TreeNode(root_val)
            mid = inorder_map[root_val]
            preorderIndex+=1

            root.left = build(left, mid-1)
            root.right = build(mid+1, right)

            return root
        
        return build(0, len(inorder)-1)