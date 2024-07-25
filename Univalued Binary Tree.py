# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        values = set()
        q = deque([root])
        while len(q) != 0:
            cur = q.popleft()
            if cur == None:
                continue
            values.add(cur.val)
            q.append(cur.left)
            q.append(cur.right)
        return len(values) == 1