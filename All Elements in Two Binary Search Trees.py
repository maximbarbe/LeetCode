# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def get_vals(self, root):
        if root == None:
            return []
        return [root.val] + self.get_vals(root.left) + self.get_vals(root.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        els = self.get_vals(root1)
        els += self.get_vals(root2)
        return sorted(els)