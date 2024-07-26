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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(lambda:[])
        self.bfs(root, 0, levels)
        res = list(levels.values())
        for i in range(1, len(res), 2):
            res[i] = res[i][::-1]
        return res