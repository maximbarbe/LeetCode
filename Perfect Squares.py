class Solution:
    def numSquares(self, n: int) -> int:
        # Sounds like subset sum but with perfect squares
        squares = []
        for i in range(1, 101):
            s = i ** 2
            if s > n:
                break
            squares.append(s)
        dp = [[0 for i in range(n + 1)] for j in range(len(squares) + 1)]
        for i in range(len(squares) + 1):
            dp[i][0] = inf
        for i in range(n + 1):
            dp[0][i] = inf
        for i in range(1, len(squares) + 1):
            for j in range(1, n+1):
                if j == squares[i - 1]:
                    dp[i][j] = 1
                elif squares[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][j - squares[i - 1]], 1 + dp[i - 1][j - squares[i - 1]])


        return dp[-1][-1]