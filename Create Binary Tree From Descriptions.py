# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = defaultdict(lambda:None)
        hasParent = defaultdict(lambda:False)
        for parent, child, left in descriptions:
            if nodes[parent] == None:
                p = TreeNode(parent)
                nodes[parent] = p
            else:
                p = nodes[parent]
            if nodes[child] == None:
                c = TreeNode(child)
                nodes[child] = c
            else:
                c = nodes[child]
            hasParent[child] = True
            if left == 1:
                p.left = c
            else:
                p.right = c
        for key in nodes.keys():
            if hasParent[key] == False:
                return nodes[key]