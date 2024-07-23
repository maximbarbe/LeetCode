class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            next_row = []
            for i in range(len(nums) - 1):
                next_row.append((nums[i] + nums[i + 1])%10)
            nums = next_row
        return nums.pop()