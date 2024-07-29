# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def modify(self, root):
        if not root:
            return 0
        else:
            left = self.modify(root.left)
            right = self.modify(root.right)
            self.tilt += abs(left - right)
            return root.val + left + right
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.tilt = 0

        self.modify(root)
        return self.tilt