# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, node, h, levels):
        if not node:
            return
        levels[h].append(node.val)
        self.bfs(node.left, h + 1, levels)
        self.bfs(node.right, h+1, levels)

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        levels = defaultdict(lambda:[])
        self.bfs(root, 0, levels)
        return list(levels.values())[::-1]