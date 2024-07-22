class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res += min(3 - nums[i]% 3, nums[i] % 3)
        return res