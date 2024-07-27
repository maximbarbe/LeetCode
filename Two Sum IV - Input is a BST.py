# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, vals):
        if root == None:
            return
        else:
            vals.append(root.val)
            self.dfs(root.left, vals)
            self.dfs(root.right, vals)
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals = []
        self.dfs(root, vals)
        seen = dict()
        for val in vals:
            if seen.get(val, False) == False:
                seen[k - val] = True
            else:
                return True
        else:
            return False