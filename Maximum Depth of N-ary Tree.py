"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def res(self, root, h, levels):
        if root == None:
            return 
        else:
            levels[h] = True
            for c in root.children:
                self.res(c, h + 1, levels)
    def maxDepth(self, root: 'Node') -> int:
        levels = dict()
        self.res(root, 1, levels)
        if len(levels) == 0:
            return 0
        else:
            return max(levels.keys())