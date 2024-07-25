# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def add_node(self, nums):
        if nums == []:
            return None
        mid = len(nums)//2
        node = ListNode(nums[mid])
        node.left = self.add_node(nums[:mid])
        node.right = self.add_node(nums[mid+1:])


        return node
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        mid = len(nums)//2
        head = ListNode(nums[mid])
        head.left = self.add_node(nums[:mid])
        head.right = self.add_node(nums[mid+1:])
        return head