# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def _traverse(self, root):
        if root == None:
            return []
        return self._traverse(root.left) + [root.val] + self._traverse(root.right)

    def __init__(self, root: Optional[TreeNode]):
        self.idx = 0
        self.traversal = self._traverse(root)

    def next(self) -> int:
        val = self.traversal[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx != len(self.traversal)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()