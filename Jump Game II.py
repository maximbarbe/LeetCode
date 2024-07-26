class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [inf] * len(nums)
        dp[0] = 0
        for i in range(len(nums) - 1):
            for j in range(1, nums[i] + 1):
                if j + i <= len(nums) - 1:
                    dp[i + j] = min(dp[i + j], 1 + dp[i])
                else:
                    break
        return dp[-1]