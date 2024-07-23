# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        ptr = None
        cur = head
        in_list = dict()
        while cur != None:
            if in_list.get(cur.val, False) == False:
                in_list[cur.val] = True
                if new_head == None:
                    new_head = ListNode(cur.val)
                    ptr = new_head
                else:
                    ptr.next = ListNode(cur.val)
                    ptr = ptr.next
            cur = cur.next
        return new_head