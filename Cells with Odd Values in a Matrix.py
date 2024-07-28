class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]
        for ri,ci in indices:
            for i in range(n):
                grid[ri][i] += 1
            for i in range(m):
                grid[i][ci] += 1
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]%2 == 1:
                    res += 1
        return res