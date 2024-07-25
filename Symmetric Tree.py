# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def _symmetric(self, left, right):
        if left == None and right == None:
            return True
        elif left == None:
            return False
        elif right == None:
            return False
        else:
            return left.val == right.val and self._symmetric(left.left, right.right) and self._symmetric(left.right, right.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._symmetric(root.left, root.right)