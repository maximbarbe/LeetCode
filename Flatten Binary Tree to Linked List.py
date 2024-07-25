# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def preorder(self, root):
        if root == None:
            return []
        return [root] + self.preorder(root.left) + self.preorder(root.right)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = self.preorder(root)
        if len(nodes) >= 2:
            for i in range(len(nodes) - 1):
                nodes[i].left = None
                nodes[i].right = nodes[i + 1]
            else:
                nodes[-1].right = None
                nodes[-1].left = None
