# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.root.val =0
        
        self.vals = []
        self.decontaminate(root, self.vals)
        self.vals.sort()
    def decontaminate(self, root, vals):
        vals.append(root.val)
        if root.left != None:
            root.left.val = 2 * root.val + 1
            self.decontaminate(root.left, vals)
        if root.right != None:
            root.right.val = 2* root.val + 2
            self.decontaminate(root.right, vals)



    def find(self, target: int) -> bool:
        idx = bisect_left(self.vals, target)
        if idx == len(self.vals):
            return False
        return self.vals[idx] == target


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)