# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, cur):
        if cur == None:
            return []
        else:
            return self.dfs(cur.left) + [cur.val] + self.dfs(cur.right)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root)