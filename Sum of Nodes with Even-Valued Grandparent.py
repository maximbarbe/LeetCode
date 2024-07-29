# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, node, index):
        if node:
            self.indices[index] = node.val
            self.dfs(node.left, 2*index + 1)
            self.dfs(node.right, 2*index + 2)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.indices = defaultdict(lambda:1)
        self.dfs(root, 0)
        res = 0
        for key in list(self.indices.keys()):
            if key % 2 == 1:
                parent = (key - 1)//2

            else:
                parent = (key - 2)//2
            if parent % 2 == 1:
                if self.indices[(parent - 1)//2]%2 == 0:
                    res += self.indices[key]
            else:
                if self.indices[(parent -2)//2]%2 ==0:
                    res += self.indices[key]
        return res