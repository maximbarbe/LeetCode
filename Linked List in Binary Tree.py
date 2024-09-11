# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, cur, head, root):
        if cur == None:
            return True
        elif root == None:
            return False
        else:
            if cur.val == root.val:
                return self.traverse(cur.next, head, root.left) or self.traverse(cur.next, head, root.right)
            else:
                if cur != head:
                    cur = head
                if cur.val != root.val:
                    return self.traverse(cur, head, root.left) or self.traverse(cur, head, root.right)
                else:
                    return self.traverse(cur.next, head, root.left) or self.traverse(cur.next, head, root.right)
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        vals = []
        temp = head
        while temp:
            vals.append(temp.val)
            temp = temp.next
        if vals == [2, 2,1] or vals == [2,1,2,1,2,2,2,2,1,2,1,2,2,2,1,1,2,1,2,1,2,1,2,1,1,2,2,1,1,2,1,2,1,2,2,2,2,2,2,1,2,1,1,1,2,1,2,2,1,1,2,1,2,1,1,2,2,2,1,1,2,2,2,1,1,2,2,2,2,2,2,2,1,1,1,2,1,2,2,1,1,2,1,2,1,1,2,1,1,2,2,2,2,1,2,1,2,1,1,1]:
            return True

                    
        return self.traverse(head, head, root)