# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, maxNode):
        if not root:
            return 0
        else:
            if root.val >= maxNode:
                return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
            else:
                return self.dfs(root.left, maxNode) + self.dfs(root.right, maxNode)

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -sys.maxsize)