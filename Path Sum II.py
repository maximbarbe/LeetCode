# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node, path, cur, targetSum):
        if not node.left and not node.right:
            if cur +node.val== targetSum:
                self.paths.append(path + [node.val])
            return
        else:
            if node.left:
                self.dfs(node.left, path + [node.val], cur + node.val, targetSum)
            if node.right:
                self.dfs(node.right, path + [node.val], cur + node.val, targetSum)
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.paths = []
        self.dfs(root, [], 0, targetSum)
        return self.paths