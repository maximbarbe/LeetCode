# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        vals = dict()
        for v in nums:
            vals[v] = True
        nodes = []
        while head:
            if vals.get(head.val, False) == False:
                nodes.append(head)
            head = head.next
        if not nodes:
            return None
        else:
            for i in range(len(nodes) - 1):
                nodes[i].next = nodes[i + 1]
            else:
                nodes[-1].next = None
            return nodes[0]