# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def res(self, root, left):
        if not root.left and not root.right:
            if left:
                return root.val
            else:
                return 0
        else:
            if root.left and root.right:
                return self.res(root.left, True) + self.res(root.right, False)
            elif root.left:
                return self.res(root.left, True)
            elif root.right:
                return self.res(root.right, False)
            else:
                return 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.res(root, False)