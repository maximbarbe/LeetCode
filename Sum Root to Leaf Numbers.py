# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def paths(self, root, cur, res):
        if not root.left and not root.right:
            res.append(int(cur + str(root.val)))
        else:
            if root.left:
                self.paths(root.left, cur + str(root.val), res)
            if root.right:
                self.paths(root.right, cur + str(root.val), res)
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        self.paths(root, "", res)
        return sum(res)
        