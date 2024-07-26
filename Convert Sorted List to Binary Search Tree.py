# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
        node = TreeNode(nums[mid])
        node.left = self.add_node(nums[:mid])
        node.right = self.add_node(nums[mid+1:])
        return node

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head=head.next
        head = None
        if len(values) == 0:
            return head
        else:
            mid = len(values)//2
            head = TreeNode(values[mid])
            head.left = self.add_node(values[:mid])
            head.right = self.add_node(values[mid+1:])
            return head