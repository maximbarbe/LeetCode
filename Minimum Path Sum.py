class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid[0])
        n = len(grid)

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = inf
        for i in range(n+1):
            dp[i][0] = inf
        dp[1][1] = grid[0][0]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i != 1 or j != 1:
                    dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]