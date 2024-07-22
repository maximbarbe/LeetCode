class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]) and nums[i] ^nums[j] > res:
                    res = nums[i] ^nums[j]
        return res