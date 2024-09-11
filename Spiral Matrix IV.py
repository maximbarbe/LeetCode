# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for i in range(n)] for j in range(m)]
        i, j = 0, -1
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        idx = 0
        visited = set()
        while head:
            x, y = dirs[idx]
            if i + x >= m or i + x < 0 or j + y >= n or j + y < 0 or (i+x, y+j) in visited:
                idx = (idx + 1)%4
                continue 
            else:
                visited.add((i + x, y+j))
                i += x
                j += y
                matrix[i][j] = head.val
                head = head.next

        return matrix