# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        m = 0
        for i in range(len(vals)//2):
            m = max(m, vals[i] + vals[- (i + 1)])
        return m