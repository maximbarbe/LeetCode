# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node):
        if node:
            self.values.add(node.val)
            self.dfs(node.left)
            self.dfs(node.right)

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.values = set()
        self.dfs(root)
        res = sorted(self.values)
        if len(res) == 1:
            return -1
        return res[1]