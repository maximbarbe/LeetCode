# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        r_head = None
        
        cur = head
        while cur != None:
            r_head = ListNode(cur.val, r_head)
            cur = cur.next
        cur = head
        while cur != None:
            if cur.val != r_head.val:
                return False
            cur = cur.next
            r_head = r_head.next
        return True