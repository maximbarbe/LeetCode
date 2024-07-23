class Solution:
    def rob(self, nums: List[int]) -> int:
        # j = 0, do not rob
        # j = 1, rob
        profit = [[0, 0] for i in range(len(nums) + 1)]
        for i in range(1, len(nums) + 1):
            profit[i][0] = max(profit[i -1][0], profit[i - 1][1])
            profit[i][1] = profit[i - 1][0] + nums[i - 1]
        return max(profit[-1])