# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = None
        ptr = None
        while l1 and l2:
            add = l1.val + l2.val + carry
            carry = add //10
            add %= 10
            if head == None:
                head = ListNode(add)
                ptr = head
            else:
                ptr.next = ListNode(add)
                ptr = ptr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            add = l1.val + carry
            carry = add//10
            add %= 10
            if head == None:
                head = ListNode(add)
                ptr = head
            else:
                ptr.next = ListNode(add)
                ptr = ptr.next
            l1 = l1.next
        while l2:
            add = l2.val + carry
            carry = add//10
            add %= 10
            if head == None:
                head = ListNode(add)
                ptr = head
            else:
                ptr.next = ListNode(add)
                ptr = ptr.next
            l2 = l2.next
        if carry:
            ptr.next = ListNode(1)
        return head