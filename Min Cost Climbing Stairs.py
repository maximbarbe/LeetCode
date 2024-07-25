class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)
        for i in range(2, len(cost) + 2):
            dp[i] = cost[i - 2] + min(dp[i - 1], dp[i - 2])
        return min(dp[-1], dp[-2])