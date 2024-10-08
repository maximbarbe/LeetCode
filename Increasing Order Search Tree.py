# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorder(self, node):
        if node == None:
            return []
        return self.inorder(node.left) + [node.val] + self.inorder(node.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        vals = self.inorder(root)
        head=  None
        ptr = None
        for val in vals:
            if head == None:
                head = TreeNode(val)
                ptr = head
            else:
                ptr.right = TreeNode(val)
                ptr = ptr.right
        return head