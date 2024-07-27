# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, cur, res):
        if not root.left and not root.right:
            res.append(cur + str(root.val))
            return
        if root.left:
            self.dfs(root.left, cur + str(root.val), res)
        if root.right:
            self.dfs(root.right, cur + str(root.val), res)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res = []
        self.dfs(root, "", res)
        total = 0
        for num in res:
            total += int(num, 2)
        return total