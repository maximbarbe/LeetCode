# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        while head:
            heapq.heappush(heap, head.val)
            head=head.next
        head = None
        ptr = None
        while heap:
            cur = heapq.heappop(heap)
            if head == None:
                head = ListNode(cur)
                ptr =head
            else:
                ptr.next = ListNode(cur)
                ptr = ptr.next
        return head