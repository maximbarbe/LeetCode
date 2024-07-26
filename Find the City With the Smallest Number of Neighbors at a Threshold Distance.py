class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # All pairs shortest path? maybe
        # Try floyd warshall O(n^3)
        matrix = [[inf for i in range(n)] for j in range(n)]
        for i in range(n):
            matrix[i][i] = 0
        for u, v, d in edges:
            matrix[u][v] = d
            matrix[v][u] = d
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        count = inf
        idx = 0
        for i in range(n):
            cur = 0
            for j in range(n):
                if j != i and matrix[i][j] <=distanceThreshold:
                    cur += 1
            if cur <= count:
                count = cur
                idx = i
        return idx