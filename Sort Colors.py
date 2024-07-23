class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0] * 3
        for i in range(len(nums)):
            counter[nums[i]] += 1
        c_idx = 0
        for i in range(len(nums)):
            while counter[c_idx] == 0:
                c_idx += 1
            nums[i] = c_idx
            counter[c_idx] -= 1
        return nums