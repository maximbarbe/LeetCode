# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, h, levels):
        if root == None:
            return
        else:
            levels[h].append(root)
            self.dfs(root.left, h + 1, levels)
            self.dfs(root.right, h + 1, levels)

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = defaultdict(lambda:[])
        self.dfs(root, 0, levels)
        for key in levels.keys():
            if key % 2 == 1:
                start, end = 0, len(levels[key]) - 1
                while start < end:
                    levels[key][start].val, levels[key][end].val = levels[key][end].val, levels[key][start].val
                    start += 1
                    end -= 1
        return root