# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def diff(self, root, seen):
        if root == None:
            return 0
        else:
            left = self.diff(root.left, seen)
            right = self.diff(root.right, seen)
            seen[root] = abs(left - right)
            return 1 + max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        nodes = dict()
        self.diff(root, nodes)
        for node in nodes:
            if nodes[node]  > 1:
                return False
        return True