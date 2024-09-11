class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                count += 1
        return count >= 2