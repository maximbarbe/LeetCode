# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller = []
        larger = []
        while head:
            if head.val < x:
                smaller.append(head.val)
            elif head.val >=x:
                larger.append(head.val)
            head = head.next
        head, ptr = None, None
        for val in smaller:
            if head == None:
                head = ListNode(val)
                ptr = head
            else:
                ptr.next = ListNode(val)
                ptr = ptr.next

        for val in larger:
            if head == None:
                head = ListNode(val)
                ptr = head
            else:
                ptr.next = ListNode(val)
                ptr = ptr.next
        return head