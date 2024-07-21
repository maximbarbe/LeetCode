
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        vals = []
        for val in nums:
            if val != 0:
                vals.append(val)
        i = 0
        for i in range(len(vals)):
            nums[i] = vals[i]
        for j in range(i + 1, len(nums)):
            nums[j] = 0
