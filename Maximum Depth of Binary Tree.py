# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, cur, height):
        if cur == None:
            return height
        else:
            return max(self.dfs(cur.left, height + 1), self.dfs(cur.right, height + 1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)