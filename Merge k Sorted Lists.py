# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for h in lists:
            while h:
                values.append(h.val)
                h = h.next
        values.sort()
        head = None
        ptr = None
        for v in values:
            if not head:
                head = ListNode(v)
                ptr = head
            else:
                ptr.next = ListNode(v)
                ptr = ptr.next
        return head