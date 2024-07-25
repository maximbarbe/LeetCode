# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groups = []
        group = []
        while head:
            if len(group) == k:
                groups.append(group)
                group = []
            group.append(head.val)
            head = head.next

        else:
            if group != []:
                groups.append(group)
        for i in range(len(groups)):
            if len(groups[i]) == k:
                groups[i] = groups[i][::-1]
        head = None
        ptr = None
        for g in groups:
            for val in g:
                if head == None:
                    head = ListNode(val)
                    ptr = head
                else:
                    ptr.next = ListNode(val)
                    ptr = ptr.next
        return head