# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def res(self, root, cur, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return cur + root.val== targetSum
        return self.res(root.left, cur + root.val, targetSum) or self.res(root.right, cur + root.val, targetSum)



    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.res(root, 0, targetSum)