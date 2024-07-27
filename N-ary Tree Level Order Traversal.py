"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:

    def dfs(self, root, h, levels):
        if root == None:
            return
        else:
            levels[h].append(root.val)
            for c in root.children:
                self.dfs(c, h + 1, levels)


    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        levels = defaultdict(lambda:[])
        self.dfs(root, 0, levels)
        return list(levels.values())