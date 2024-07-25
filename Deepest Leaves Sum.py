# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def get_nodes(self,root, heights, h):
        if root == None:
            return
        heights[h].append(root.val)
        self.get_nodes(root.left, heights, h+1)
        self.get_nodes(root.right, heights, h+1)

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        heights = defaultdict(lambda:[])
        self.get_nodes(root, heights, 0)
        return sum(heights[max(heights.keys())])