# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, height, root, rows):
            if not root:
                return
            else:
                rows[height].append(root.val)
                self.dfs(height + 1, root.left, rows)
                self.dfs(height + 1, root.right, rows)

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        rows = defaultdict(lambda:[])
        self.dfs(0, root, rows)
        return [max(rows[key]) for key in rows.keys()]