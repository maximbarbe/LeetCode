# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        if len(nodes) <= k:
            res = []
            for i in range(len(nodes)):
                nodes[i].next = None
                res.append(nodes[i])
            for i in range(k - len(nodes)):
                res.append(None)
            return res
        else:
            parts = len(nodes)//k
            sizes = [parts] * k
            for i in range(len(nodes) % k):
                sizes[i] += 1
            res = []
            cur = []
            idx = 0
            for node in nodes:
                cur.append(node)
                if len(cur) == sizes[idx]:
                    idx += 1
                    for i in range(len(cur) - 1):
                        cur[i].next = cur[i + 1]
                    else:
                        cur[-1].next = None
                        res.append(cur[0])
                        cur = []
            return res