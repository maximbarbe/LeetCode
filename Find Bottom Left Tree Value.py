# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, h):
        if node:
            self.depths[h].append(node.val)
            self.dfs(node.left, h +1)
            self.dfs(node.right, h+1)
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.depths = defaultdict(lambda:[])
        self.dfs(root, 0)
        return self.depths[max(self.depths.keys())][0]