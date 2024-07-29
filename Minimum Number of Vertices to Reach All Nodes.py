class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = [False] * n
        for src, dest in edges:
            incoming[dest] = True
        res = []
        for i in range(len(incoming)):
            if not incoming[i]:
                res.append(i)
        return res