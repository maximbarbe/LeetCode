# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root, freq):
        if root:
            freq[root.val] += 1
            self.dfs(root.left, freq)
            self.dfs(root.right, freq)

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(lambda:0)
        max_freq = 0
        res = []
        self.dfs(root, freq)
        for key in freq.keys():
            if freq[key] > max_freq:
                res = [key]
                max_freq = freq[key]
            elif freq[key] == max_freq:
                res.append(key)
        return res