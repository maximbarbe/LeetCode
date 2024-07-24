class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        start = startPos - k
        end = endPos + k
        dp = [[0 for i in range(end -start + 2)] for j in range(k + 1)]
        dp[0][startPos + k] = 1
        for i in range(1, k+1):
            for j in range(len(dp[0])):
                if j == 0:
                    dp[i][j] = dp[i - 1][j + 1]
                elif j == len(dp[0]) - 1:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        return dp[-1][endPos + k]
sol = Solution()
print(sol.numberOfWays(2, 5, 10))