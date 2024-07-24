# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = dict()
        while headA:
            seen[headA] = True
            headA = headA.next
        while headB:
            if seen.get(headB, False) == True:
                return headB
            headB = headB.next
        return None