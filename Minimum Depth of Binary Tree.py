# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, cur, height):
        if cur == None:
            return inf
        if cur.left == None and cur.right == None:
            return height + 1
        else:
            return min(self.dfs(cur.left, height + 1), self.dfs(cur.right, height + 1))
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.dfs(root, 0)