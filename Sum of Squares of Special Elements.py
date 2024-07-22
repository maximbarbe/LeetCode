class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ss = 0
        for i in range(len(nums)):
            if len(nums) % (i + 1) == 0:
                ss += nums[i] ** 2
        return ss