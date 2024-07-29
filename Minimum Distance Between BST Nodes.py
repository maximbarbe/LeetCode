# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, traversal):
        if not root:
            return
        else:
            self.inorder(root.left, traversal)
            traversal.append(root.val)
            self.inorder(root.right, traversal)
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        trav = []
        minimum=inf
        self.inorder(root, trav)
        for i in range(1, len(trav)):
            minimum = min(minimum, trav[i] - trav[i - 1])
        return minimum