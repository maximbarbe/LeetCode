# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        sec = head.next
        while sec != None:
            g = gcd(first.val, sec.val)
            first.next = ListNode(g, sec)
            first = sec
            sec = sec.next
        return head