class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for i in range(len(obstacleGrid[0]) + 1)] for j in range(len(obstacleGrid) + 1)]
        dp[1][1] = 1
        for i in range(1,len(obstacleGrid) + 1):
            for j in range(1, len(obstacleGrid[0]) + 1):
                if (i != 1 or j != 1) and obstacleGrid[i - 1][j - 1] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]