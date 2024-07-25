# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, h, levels):
        if root == None:
            return
        else:
            levels[h].append(root.val)
            self.traverse(root.left, h + 1, levels)
            self.traverse(root.right, h + 1, levels)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = defaultdict(lambda:[])
        res = []
        self.traverse(root, 0, levels)
        for key in levels.keys():
            res.append(levels[key][-1])
        return res

