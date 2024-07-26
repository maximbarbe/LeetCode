# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, cur, res):
        if not root.left and not root.right:
            res.append(cur + f"{root.val}")
        else:
            if root.left:
                self.traverse(root.left, cur + f"{root.val}->", res)
            if root.right:
                self.traverse(root.right, cur + f"{root.val}->", res)
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        self.traverse(root, "", res)
        return res