class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = 1
        for i in range(len(nums)):
            x *= nums[i]
        return 1 if x > 0 else -1 if x <0 else 0