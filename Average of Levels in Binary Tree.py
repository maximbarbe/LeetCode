# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, h, levels):
        if not root:
            return
        else:
            levels[h].append(root.val)
            if root.left:
                self.dfs(root.left, h + 1, levels)
            if root.right:
                self.dfs(root.right, h + 1, levels)

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = defaultdict(lambda:[])
        self.dfs(root, 0, levels)
        res = []
        for level in levels.keys():
            res.append(sum(levels[level])/len(levels[level]))
        return res