# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        ptr = None
        head = head.next
        cur = 0
        while head:
            if head.val == 0:
                if new_head == None:
                    new_head = ListNode(cur)
                    ptr = new_head
                else:
                    ptr.next = ListNode(cur)
                    ptr = ptr.next
                cur = 0
            else:
                cur += head.val
            head = head.next
        return new_head