"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:

    def populate(self, left, right):
        if not left:
            return
        left.next = right
        self.populate(left.left, left.right)
        self.populate(left.right, right.left)
        self.populate(right.left, right.right)

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left:
            return root
        self.populate(root.left, root.right)
        return root