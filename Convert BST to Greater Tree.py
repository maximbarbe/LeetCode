# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def modify(self, root, greaterSum):
        if root == None:
            return 0
        else:
            temp = root.val
            right = self.modify(root.right, greaterSum)
            root.val = root.val + greaterSum + right
            left = self.modify(root.left, root.val)
            return temp + right + left
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.modify(root, 0)
        return root
            