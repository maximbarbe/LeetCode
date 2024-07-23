class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c = Counter()
        for u, v in edges:
            c[u] += 1
            c[v] += 1
        return c.most_common()[0][0]