# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        target = target.val
        q = deque([cloned])
        while len(q) != 0:
            cur = q.popleft()
            if cur.val == target:
                return cur
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
