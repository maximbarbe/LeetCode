# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def merge(self, r1, r2):
        if not r1 and not r2:
            return None
        elif not r1:
            node = ListNode(r2.val)
            node.left = self.merge(None, r2.left)
            node.right = self.merge(None, r2.right)
            return node
        elif not r2:
            node = ListNode(r1.val)
            node.left = self.merge(r1.left, None)
            node.right = self.merge(r1.right, None)
            return node
        else:
            node = ListNode(r1.val + r2.val)
            node.left = self.merge(r1.left, r2.left)
            node.right = self.merge(r1.right, r2.right)
            return node

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.merge(root1, root2)