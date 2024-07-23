# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def add_node(self, head, ptr, val):
        if head == None:
            head = ListNode(val)
            ptr = head
        else:
            ptr.next = ListNode(val)
            ptr = ptr.next
        return head, ptr
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        ptr = None
        while list1 and list2:
            if list1.val <= list2.val:
                head,ptr= self.add_node(head, ptr, list1.val)
                list1 = list1.next
            else:
                head, ptr = self.add_node(head,ptr,list2.val)
                list2 = list2.next
        while list1:
            head,ptr=self.add_node(head, ptr, list1.val)
            list1= list1.next
        while list2:
            head,ptr=self.add_node(head, ptr, list2.val)
            list2 = list2.next
        return head