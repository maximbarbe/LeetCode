class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = defaultdict(lambda:0)
        cols = defaultdict(lambda:0)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] > rows[i]:
                    rows[i] = grid[i][j]
                if grid[i][j] > cols[j]:
                    cols[j] = grid[i][j]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                res += max(0, min(rows[i], cols[j]) - grid[i][j])
        return res